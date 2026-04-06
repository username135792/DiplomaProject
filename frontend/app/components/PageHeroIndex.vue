<!-- components/PageHero.vue -->
<template>
  <div class="flex-1">
    <UPageHero :ui="uiConfig">
      <!-- Left content -->
      <template #title>
        <h1 class="text-2xl text-black dark:text-white font-bold">
          {{ title }}
        </h1>
      </template>

      <template #description>
        <p class="text-lg text-gray-500 dark:text-gray-400 mt-4">
          {{ description }}
        </p>
      </template>

      <template #links>
        <UButton 
          :label="buttonLabel" 
          :to="buttonLink"
          color="primary" 
          size="xl" 
        />
      </template>

      <!-- Right image -->
      <template #default>
        <img 
          :src="image" 
          :alt="imageAlt"
          class="rounded-lg shadow-2xl hidden lg:block" 
        />
      </template>
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
  buttonLabel: {
    type: String,
    default: 'Learn More'
  },
  buttonLink: {
    type: String,
    default: '#'
  },
  image: {
    type: String,
    required: true
  },
  imageAlt: {
    type: String,
    default: 'Hero image'
  }
})

// Extract UI config to keep template clean
const uiConfig = {
  container: 'items-center grid-cols-2 lg:gap-10 sm:py-6 md:py-6 lg:py-12 xl:py-12'
}
</script>