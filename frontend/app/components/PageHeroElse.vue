<!-- components/PageHeroElse.vue -->
<template>
  <div class="flex-1">
    <UPageHero
      :ui="uiConfig"
      :class="image ? '' : ''"
    >
      <!-- Image with rounded corners and padding -->
      <div v-if="image" class="absolute inset-0 -z-10 flex items-center justify-center p-4">
        <div class="relative w-full h-full">
          <div class="absolute inset-0 bg-black/50 rounded-2xl"></div>
          <img
            :src="image"
            :alt="imageAlt"
            class="w-full h-full object-cover rounded-2xl"
          />
        </div>
      </div>

      <!-- Title - bigger text, aligned right with margin -->
      <template #title>
        <div class="text-left mr-8">
          <h1 class="text-4xl lg:text-5xl text-white font-bold relative z-10">
            {{ title }}
          </h1>
        </div>
      </template>

      <!-- Description - bigger text, aligned right with margin -->
      <template #description>
        <div class="text-left mr-8">
          <p class="text-xl lg:text-2xl text-gray-200 mt-6 relative z-10">
            {{ description }}
          </p>
        </div>
      </template>

      <!-- Removed button template -->
    </UPageHero>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  image: {
    type: String,
    required: true,
    default: ''
  },
  imageAlt: {
    type: String,
    default: 'Hero image'
  }
})

// UI Config for full-width background
const uiConfig = {
  root: 'w-full relative',
  container: 'max-w-none w-full px-0 py-12 lg:py-24' // Removed max-width, added padding
}
</script>