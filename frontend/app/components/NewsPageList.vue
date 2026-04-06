<template>
  <div class="flex-1">
    <UContainer :ui="uiConfig">
      <div v-if="title || subtitle" class="text-center mb-12 lg:mb-16">
        <h2 v-if="title" class="text-4xl lg:text-5xl font-bold text-white mb-4">
          {{ title }}
        </h2>
        <p v-if="subtitle" class="text-xl text-gray-400 max-w-3xl mx-auto">
          {{ subtitle }}
        </p>
      </div>
      <UPageList :divide="divide">
        <div
          v-for="(item, index) in items"
          :key="index"
          class="py-8"
        >
          <div class="flex flex-col lg:flex-row items-start lg:items-center gap-6 lg:gap-10">
            <div class="flex-1">

              <h3 v-if="item.title" class="text-2xl lg:text-3xl font-bold text-white mb-4">
                {{ item.title }}
              </h3>

              <p v-if="item.description" class="text-gray-400 text-lg">
                {{ item.description }}
              </p>
            </div>

            <div v-if="item.photo" class="lg:w-1/3">
              <div class="relative overflow-hidden rounded-2xl">
                <img
                  :src="item.photo"
                  :alt="item.photoAlt || item.title || 'News image'"
                  class="w-full h-64 lg:h-80 object-cover hover:scale-105 transition-transform duration-300"
                />
              </div>
            </div>
          </div>
        </div>
      </UPageList>
    </UContainer>
  </div>
</template>


<script setup>
import { UPageList } from '#components'
defineProps({
  // Main title for the news list section
  title: {
    type: String,
    default: ''
  },
  // Subtitle/description under the title
  subtitle: {
    type: String,
    default: ''
  },
  // Array of news item objects
  items: {
    type: Array,
    required: true,
    default: () => [],
    validator: (items) => {
      return items.every(item =>
        typeof item === 'object' &&
        (item.title || item.description || item.photo) // At least one of these is required
      )
    }
  },
  // Whether to show dividers between items
  divide: {
    type: Boolean,
    default: true
  }
})

// UI Config for container
const uiConfig = {
  class: 'py-12 lg:py-20'
}

</script>