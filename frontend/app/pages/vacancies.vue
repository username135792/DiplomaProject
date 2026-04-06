<template>
  <PageHeroElse
    title="Test"
    description="testtesttest"
    image="/images/office.png"
    image-alt="Office workspace"
  />
    <div class="max-w-5xl mx-auto py-12 px-6">
      <h1 class="text-4xl font-bold mb-8">Open Vacancies</h1>
      <p class="text-gray-600 mb-10">Join our team! Here are current job opportunities.</p>
      
      <!-- We will later fill this with real jobs from Django -->
      <div class="space-y-6">
        <UCard v-for="n in 3" :key="n" class="p-6">
          <h2 class="text-2xl font-semibold">Software Engineer</h2>
          <p class="text-green-600">Full-time • Remote</p>
          <UButton class="mt-4">View Details</UButton>
        </UCard>
      </div>
    </div>
  </template>