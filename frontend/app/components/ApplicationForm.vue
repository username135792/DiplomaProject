<template>
  <div>
    <div class="text-center py-6 border-b border-gray-800 mb-6">
      <UIcon name="i-lucide-file-text" class="h-12 w-12 mx-auto mb-4 text-primary-500" />
      <h2 class="text-2xl font-bold text-white">Форма отклика на вакансию</h2>
      <p class="text-sm text-gray-400 mt-2" v-if="vacancy">Вакансия: {{ vacancy.title }}</p>
    </div>

    <UForm :state="formState" @submit="handleSubmit" class="space-y-6">
      <!-- Personal Information Section -->
      <div class="space-y-4">
        <h3 class="text-lg font-semibold text-white border-b border-gray-800 pb-2">Личные данные</h3>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <UFormField label="Фамилия" name="lastName" required>
            <UInput v-model="formState.lastName" placeholder="Введите фамилию" />
          </UFormField>

          <UFormField label="Имя" name="firstName" required>
            <UInput v-model="formState.firstName" placeholder="Введите имя" />
          </UFormField>

          <UFormField label="Отчество" name="middleName">
            <UInput v-model="formState.middleName" placeholder="Введите отчество" />
          </UFormField>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <UFormField label="Дата рождения" name="birthDate" required>
            <UInputDate v-model="formState.birthDate" icon="i-lucide-calendar" />
          </UFormField>

          <UFormField label="Номер телефона" name="phone" required>
            <UInput v-model="formState.phone" placeholder="+7 (XXX) XXX-XX-XX" type="tel" />
          </UFormField>
        </div>

        <UFormField label="E-mail" name="email" required>
          <UInput v-model="formState.email" placeholder="example@email.com" type="email" />
        </UFormField>
      </div>

      <!-- Address Information Section -->
      <div class="space-y-4">
        <h3 class="text-lg font-semibold text-white border-b border-gray-800 pb-2">Адресные данные</h3>

        <UFormField label="Адрес прописки" name="registrationAddress" required>
          <UInput v-model="formState.registrationAddress" placeholder="Введите адрес прописки" />
        </UFormField>

        <UFormField label="Адрес проживания" name="residenceAddress" required>
          <UInput v-model="formState.residenceAddress" placeholder="Введите адрес проживания" />
        </UFormField>

        <UFormField label="Гражданство" name="citizenship" required>
          <UInput v-model="formState.citizenship" placeholder="Введите гражданство" />
        </UFormField>
      </div>

      <!-- Education and Work Section -->
      <div class="space-y-4">
        <h3 class="text-lg font-semibold text-white border-b border-gray-800 pb-2">Образование и опыт работы</h3>

        <UFormField label="Образование" name="education" required>
          <UInput v-model="formState.education" placeholder="Введите образование" />
        </UFormField>

        <UFormField label="Специальность" name="specialty" required>
          <UInput v-model="formState.specialty" placeholder="Введите специальность" />
        </UFormField>

        <UFormField label="Стаж муниципальной службы" name="municipalExperience">
          <UInput v-model="formState.municipalExperience" placeholder="Введите стаж" />
        </UFormField>

        <UFormField label="Трудовая деятельность (сведения из трудовой книжки)" name="workExperience">
          <UTextarea v-model="formState.workExperience" placeholder="Опишите трудовую деятельность" :rows="3" />
        </UFormField>
      </div>

      <!-- Family Information Section -->
      <div class="space-y-4">
        <h3 class="text-lg font-semibold text-white border-b border-gray-800 pb-2">Семейное положение</h3>

        <UFormField label="Семейное положение" name="maritalStatus" required>
          <URadioGroup v-model="formState.maritalStatus" :options="maritalStatusOptions" />
        </UFormField>

        <UFormField label="Наличие детей" name="children">
          <UInput v-model="formState.children" placeholder="Укажите количество и возраст детей" />
        </UFormField>
      </div>

      <!-- File Upload Section -->
      <div class="space-y-4">
        <h3 class="text-lg font-semibold text-white border-b border-gray-800 pb-2">Прикрепленные файлы</h3>

        <UFormField label="Фото" name="photo">
          <UFileUpload v-model="formState.photo" accept="image/*" label="Загрузите ваше фото" description="JPG, PNG или GIF (макс. 5MB)" />
        </UFormField>

        <UFormField label="Файл с резюме" name="resume" required>
          <UFileUpload v-model="formState.resume" accept=".pdf,.doc,.docx" label="Загрузите ваше резюме" description="PDF, DOC или DOCX (макс. 10MB)" />
        </UFormField>
      </div>

      <!-- Additional Information -->
      <div class="space-y-4">
        <UFormField label="О вакансии узнал(а)" name="vacancySource">
          <UTextarea v-model="formState.vacancySource" placeholder="Укажите, где вы узнали о вакансии" :rows="2" />
        </UFormField>
      </div>

      <!-- Action buttons -->
      <div class="flex justify-end gap-3 mt-8 pt-6 border-t border-gray-800">
        <UButton
          label="Отмена"
          color="neutral"
          variant="outline"
          @click="$emit('cancel')"
        />
        <UButton
          label="Отправить"
          color="primary"
          type="submit"
          :loading="isSubmitting"
        />
      </div>
    </UForm>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'

const props = defineProps({
  vacancy: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['submit', 'cancel'])

const isSubmitting = ref(false)

// Form state
const formState = reactive({
  lastName: '',
  firstName: '',
  middleName: '',
  birthDate: null,
  phone: '',
  email: '',
  registrationAddress: '',
  residenceAddress: '',
  citizenship: '',
  education: '',
  specialty: '',
  municipalExperience: '',
  workExperience: '',
  maritalStatus: '',
  children: '',
  photo: null,
  resume: null,
  vacancySource: ''
})

// Marital status options
const maritalStatusOptions = [
  { value: 'single', label: 'Холост/Не замужем' },
  { value: 'married', label: 'Женат/Замужем' },
  { value: 'divorced', label: 'Разведен(а)' },
  { value: 'widowed', label: 'Вдовец/Вдова' }
]

const handleSubmit = async () => {
  isSubmitting.value = true

  try {
    // For now, just emit the form data
    // In a real app, you would validate and send to backend here
    emit('submit', { ...formState })

    // Reset form after successful submission
    Object.keys(formState).forEach(key => {
      if (key === 'maritalStatus') {
        formState[key] = ''
      } else if (key === 'photo' || key === 'resume') {
        formState[key] = null
      } else {
        formState[key] = ''
      }
    })
  } catch (error) {
    console.error('Form submission error:', error)
  } finally {
    isSubmitting.value = false
  }
}
</script>