<template>
  <div class="flex-1 pb-6">
    <!-- Application Form Modal -->
    <UModal v-model:open="isApplicationFormOpen" title="Отклик на вакансию">
      <template #body>
        <ApplicationForm :vacancy="selectedVacancy" @submit="handleFormSubmit" @cancel="closeApplicationForm" />
      </template>
    </UModal>

    <UContainer :ui="uiConfig">
      <!-- Header Section -->
      <div class="text-center mb-6">
        <h2 class="text-3xl lg:text-4xl font-bold text-gray-900 dark:text-white mb-4">
          {{ title }}
        </h2>
        <p v-if="subtitle" class="text-lg text-gray-500 dark:text-gray-400 max-w-3xl mx-auto">
          {{ subtitle }}
        </p>
      </div>

      <!-- Vacancies Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <UCard
          v-for="(vacancy, index) in vacancies"
          :key="index"
          class="bg-white/80 dark:bg-transparent backdrop-blur-sm ring-1 ring-gray-200 dark:ring-gray-800 hover:border-green-500/50 transition-all duration-300 hover:shadow-lg hover:shadow-green-500/10"
          :ui="{
            root: 'h-full flex flex-col',
            body: 'flex-1 p-4 sm:p-6',
            footer: 'p-4 sm:px-6'
          }"
        >
          <!-- Vacancy Header -->
          <template #header>
            <div class="flex justify-between items-start">
              <div>
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-2">{{ vacancy.title }}</h3>
                <div class="flex items-center gap-2 text-gray-500 dark:text-gray-400">
                  <UIcon name="i-lucide-building" class="h-4 w-4" />
                  <span>{{ vacancy.company }}</span>
                </div>
              </div>
              <UBadge
                v-if="vacancy.isNew"
                color="green"
                variant="subtle"
                size="sm"
              >
                Новое
              </UBadge>
            </div>
          </template>

          <!-- Vacancy Details -->
          <div class="space-y-3 mb-6">
            <!-- Location -->
            <div class="flex items-center gap-2 text-gray-500 dark:text-gray-400">
              <UIcon name="i-lucide-map-pin" class="h-4 w-4" />
              <span>{{ vacancy.location }}</span>
            </div>

            <!-- Salary -->
            <div class="flex items-center gap-2 text-green-600 dark:text-green-400 font-semibold">
              <UIcon name="i-lucide-wallet" class="h-4 w-4" />
              <span>{{ vacancy.salary }}</span>
            </div>

            <!-- Employment Type -->
            <div class="flex items-center gap-2 text-gray-500 dark:text-gray-400">
              <UIcon name="i-lucide-briefcase" class="h-4 w-4" />
              <span>{{ vacancy.employmentType }}</span>
            </div>

            <!-- Experience -->
            <div class="flex items-center gap-2 text-gray-500 dark:text-gray-400">
              <UIcon name="i-lucide-award" class="h-4 w-4" />
              <span>Опыт: {{ vacancy.experience }}</span>
            </div>
          </div>

          <!-- Skills Tags -->
          <div class="flex flex-wrap gap-2 mb-6">
            <UBadge
              v-for="(skill, skillIndex) in vacancy.skills"
              :key="skillIndex"
              color="gray"
              variant="subtle"
              size="sm"
            >
              {{ skill }}
            </UBadge>
          </div>

          <!-- Action Buttons -->
          <template #footer>
            <div class="flex gap-3">
              <UButton
                label="Подробнее"
                color="primary"
                variant="solid"
                class="bg-primary-500 text-gray-900 dark:text-white hover:bg-primary-600 flex-1"
                :to="vacancy.detailsLink"
              />
              <UButton
                label="Откликнуться"
                color="green"
                variant="outline"
                class="bg-primary-500 text-gray-900 dark:text-white hover:bg-primary-600 flex-1"
                @click="openApplicationForm(vacancy)"
              />
            </div>
          </template>
        </UCard>
      </div>

      <!-- No Vacancies Message -->
      <div
        v-if="vacancies.length === 0"
        class="text-center py-12"
      >
        <UIcon name="i-lucide-search-x" class="h-16 w-16 text-gray-600 mx-auto mb-4" />
        <h3 class="text-xl font-semibold text-gray-700 dark:text-gray-300 mb-2">Вакансии не найдены</h3>
        <p class="text-gray-500 dark:text-gray-500">Попробуйте изменить параметры поиска</p>
      </div>
    </UContainer>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ApplicationForm from './ApplicationForm.vue'

// Reactive state
const config = useRuntimeConfig()
const isApplicationFormOpen = ref(false)
const selectedVacancy = ref(null)

const isSubmitting = ref(false)
const submitStatus = ref(null) // null | 'success' | 'error'

// Methods
const openApplicationForm = (vacancy) => {
  submitStatus.value = null
  selectedVacancy.value = vacancy
  isApplicationFormOpen.value = true
}

const closeApplicationForm = () => {
  isApplicationFormOpen.value = false
  selectedVacancy.value = null
  submitStatus.value = null
}

const handleFormSubmit = async (formData) => {
  isSubmitting.value = true
  submitStatus.value = null

  try {
    const data = new FormData()
    data.append('vacancy_title', selectedVacancy.value?.title || '')

    for (const [key, value] of Object.entries(formData)) {
      if (value instanceof File || (Array.isArray(value) && value[0] instanceof File)) {
        // Handle file uploads — UFileUpload returns an array of Files
        const files = Array.isArray(value) ? value : [value]
        for (const file of files) {
          if (file instanceof File) {
            data.append(key, file)
          }
        }
      } else if (value !== null && value !== undefined) {
        let fieldName = key
          .replace(/([A-Z])/g, '_$1')
          .toLowerCase()

        // Handle special field mappings
        const fieldMap = {
          'last_name': 'last_name',
          'first_name': 'first_name',
          'middle_name': 'middle_name',
          'birth_date': 'birth_date',
          'registration_address': 'registration_address',
          'residence_address': 'residence_address',
          'municipal_experience': 'municipal_experience',
          'work_experience': 'work_experience',
          'marital_status': 'marital_status',
          'vacancy_source': 'vacancy_source'
        }
        fieldName = fieldMap[fieldName] || fieldName

        if (value instanceof Date) {
          data.append(fieldName, value.toISOString().split('T')[0])
        } else {
          data.append(fieldName, value)
        }
      }
    }

    const response = await $fetch(`${config.public.apiBaseUrl}/api/apply/`, {
      method: 'POST',
      body: data
    })

    submitStatus.value = 'success'
    setTimeout(() => closeApplicationForm(), 2000)
  } catch (error) {
    console.error('Server error:', error.data || error.message || error)
    submitStatus.value = 'error'
  } finally {
    isSubmitting.value = false
  }
}

// Props
defineProps({
  // Main title for the vacancies section
  title: {
    type: String,
    default: 'Последние вакансии'
  },
  // Subtitle/description under the title
  subtitle: {
    type: String,
    default: 'Найдите подходящую вакансию для вашей карьеры'
  },
  // Array of vacancy objects
  vacancies: {
    type: Array,
    required: true,
    default: () => [],
    validator: (vacancies) => {
      return vacancies.every(vacancy =>
        typeof vacancy === 'object' &&
        vacancy.title &&
        vacancy.company &&
        vacancy.location &&
        vacancy.salary
      )
    }
  }
})

// Methods
const handleQuickApply = (vacancy) => {
  // Emit event or handle quick apply logic
  console.log('Quick apply for:', vacancy.title)
  // In a real app: emit('quick-apply', vacancy)
}

// UI Config for container
const uiConfig = {
  class: 'py-12 lg:py-20'
}
</script>