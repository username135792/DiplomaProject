<!-- components/PageColumns.vue -->
<template>
  <div class="flex-1 py-6">
    <UContainer :ui="uiConfig">
      <!-- Title section -->
      <div v-if="title || subtitle" class="text-center mb-12 lg:mb-16">
        <h2 v-if="title" class="text-4xl lg:text-5xl font-bold text-white mb-4">
          {{ title }}
        </h2>
        <p v-if="subtitle" class="text-xl text-gray-400 max-w-3xl mx-auto">
          {{ subtitle }}
        </p>
      </div>

      <!-- Actual Nuxt UI PageColumns style using CSS columns -->
      <UPageColumns :ui="pageColumnsUi">
        <div
          v-for="(column, index) in columns"
          :key="index"
          class="break-inside-avoid-column will-change-transform"
        >
          <!-- Column container with background and rounded rectangle -->
          <div class="bg-gray-900/50 border border-gray-800 rounded-2xl p-6 lg:p-8">
            <!-- Column icon (optional) -->
            <div v-if="column.icon" class="mb-6">
              <div class="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-primary/10">
                <UIcon :name="column.icon" class="h-8 w-8 text-primary" />
              </div>
            </div>

            <!-- Column title -->
            <h3 v-if="column.title" class="text-2xl lg:text-3xl font-bold text-white mb-4">
              {{ column.title }}
            </h3>

            <!-- Column description -->
            <p v-if="column.description" class="text-gray-400 text-lg mb-6">
              {{ column.description }}
            </p>

            <!-- Column button (optional) -->
            <div v-if="column.buttonLabel" class="mt-6">
              <UButton
                v-if="column.buttonLink"
                :label="column.buttonLabel"
                :to="column.buttonLink"
                color="primary"
                variant="ghost"
                size="lg"
                :ui="{ rounded: 'rounded-lg' }"
              />
              <UButton
                v-else
                :label="column.buttonLabel"
                color="primary"
                variant="ghost"
                size="lg"
                :ui="{ rounded: 'rounded-lg' }"
              />
            </div>
          </div>
        </div>
      </UPageColumns>
    </UContainer>
  </div>
</template>

<script setup>
const props = defineProps({
  // Main title for the columns section
  title: {
    type: String,
    default: ''
  },
  // Subtitle/description under the title
  subtitle: {
    type: String,
    default: ''
  },
  // Array of column objects
  columns: {
    type: Array,
    required: true,
    default: () => [],
    validator: (columns) => {
      return columns.every(col =>
        typeof col === 'object' &&
        (col.title || col.description) // At least title or description is required
      )
    }
  },
  // Number of columns for responsive design
  columnsCount: {
    type: Number,
    default: 3,
    validator: (value) => [1, 2, 3, 4].includes(value)
  }
})

// UI Config for container
const uiConfig = {
  class: 'py-12 lg:py-20'
}

// UPageColumns UI configuration based on columnsCount
const pageColumnsUi = {
  base: (() => {
    switch (props.columnsCount) {
      case 1:
        return 'columns-1 gap-8 space-y-8 *:break-inside-avoid-column *:will-change-transform'
      case 2:
        return 'columns-1 md:columns-2 gap-8 space-y-8 *:break-inside-avoid-column *:will-change-transform'
      case 3:
        return 'columns-1 md:columns-2 lg:columns-3 gap-8 space-y-8 *:break-inside-avoid-column *:will-change-transform'
      case 4:
        return 'columns-1 md:columns-2 lg:columns-3 xl:columns-4 gap-8 space-y-8 *:break-inside-avoid-column *:will-change-transform'
      default:
        return 'columns-1 md:columns-2 lg:columns-3 gap-8 space-y-8 *:break-inside-avoid-column *:will-change-transform'
    }
  })()
}
</script>