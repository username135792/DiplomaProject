<template>
  <PageHeroElse
    title="Test"
    description="testtesttest"
    image="/images/office.png"
    image-alt="Office workspace"
  />
    <div class="max-w-2xl mx-auto py-12 px-6">
      <h1 class="text-4xl font-bold text-gray-900 dark:text-white mb-8">Get in Touch</h1>
        <!-- We can make a real contact form later -->
        <UInput placeholder="Your email" />
        <UTextarea placeholder="Message" class="mt-4" />
        <UButton type="submit" class="bg-primary-500 text-gray-900 dark:text-white hover:bg-primary-600 mt-6">Send Message</UButton>
    </div>
  </template>