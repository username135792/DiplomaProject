<template>
  <!-- Первое главное -->
  <PageHeroIndex
    title="Успешная команда - успешный город"
    description="Отправляй свое резюме сейчас и наш специалист свяжется с вами"
    button-label="Наши вакансии"
    button-link="/vacancies"
    image="/images/office.png"
    image-alt="Office workspace"
  />

  <!-- Вот с кем мы работаем -->
  <div>
    <USeparator 
      label="Нам доверяют" 
      class="my-6"
    />
  </div>

  <!-- Листающиеся логотипы -->
  <!-- TODO: при маленком разрешении они стоят в ряд не шевелясь -->
  <div class="group **:data-marquee:hover:[animation-play-state:paused]">
    <UMarquee
      pause-on-hover
      :overlay="false"
      :ui="{ root: '[--gap:16px]' }"
    >
      <NuxtLink 
        v-for="(icon, index) in [
          { url: 'https://github.com', icon: 'i-simple-icons-github' },
          { url: 'https://discord.com', icon: 'i-simple-icons-discord' },
          { url: 'https://x.com', icon: 'i-simple-icons-x' },
          { url: 'https://instagram.com', icon: 'i-simple-icons-instagram' },
          { url: 'https://linkedin.com', icon: 'i-simple-icons-linkedin' },
          { url: 'https://facebook.com', icon: 'i-simple-icons-facebook' }
        ]"
        :key="index"
        :to="icon.url"
        target="_blank"
        class="flex items-center justify-center px-8 mb-6"
      >
        <UIcon :name="icon.icon" class="h-12 w-12 opacity-75 hover:opacity-100 transition" />
      </NuxtLink>
    </UMarquee>
  </div>

  <!-- Деятельность -->
  <UContainer class="py-6 lg:py-12">
    <UBlogPosts 
      class="grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 lg:gap-6"
      :posts="posts"
    />
  </UContainer>

  <!-- Почему работать именно с нами -->
  <UContainer class="py-6 lg:py-12">
    <!-- Header -->
    <div class="max-w-2xl mb-6">
      <h2 class="text-3xl lg:text-5xl font-bold text-white mb-4">
        Почему именно мы?
      </h2>
      <p class="text-gray-400 text-lg">
        Вот коротко почему именно мы
      </p>
    </div>
    <!-- Features Grid -->
    <UPageGrid class="lg:grid-cols-3 gap-8">
      <UPageCard
        v-for="feature in features"
        :key="feature.title"
        :title="feature.title"
        :description="feature.description"
        :icon="feature.icon"
        class="bg-gray-900/50 border-gray-800"
      />
    </UPageGrid>
  </UContainer>
  <!-- FAQ -->
  <UContainer class="py-6 lg:py-12">
    <!-- Header -->
    <div class=" max-w-2xl mx-2 mb-2">
      <h2 class="text-3xl lg:text-5xl font-bold text-white mb-4">
        Часто Задаваемые <span class="text-green-500">Вопросы</span>
      </h2>
      <p class="text-gray-400 text-lg">
        Everything you need to know about our productivity platform.
      </p>
    </div>

    <!-- FAQ Accordion -->
    <div class="py-6 lg:py-12">
      <UAccordion
        :items="FAQ_items"
        :ui="{
          wrapper: 'flex flex-col gap-4',
          item: 'bg-gray-900/50 border border-gray-800 rounded-lg overflow-hidden',
          header: 'px-4 py-2 text-white font-medium hover:bg-gray-800/50 transition',
          body: 'px-6 py-2 text-gray-400',
          trailing: 'text-orange-500'
        }"
        multiple
      />
    </div>
  </UContainer>
</template>

<script setup>
const features = [
  {
    title: 'Тестовый заголовок',
    description: 'Мы то-то и то-то',
    icon: 'i-lucide-sparkles'
  },
  {
    title: 'Тестовый заголовок',
    description: 'Мы то-то и то-то',
    icon: 'i-lucide-sparkles'
  },
  {
    title: 'Тестовый заголовок',
    description: 'Мы то-то и то-то',
    icon: 'i-lucide-sparkles'
  },
  {
    title: 'Тестовый заголовок',
    description: 'Мы то-то и то-то',
    icon: 'i-lucide-sparkles'
  },
  {
    title: 'Тестовый заголовок',
    description: 'Мы то-то и то-то',
    icon: 'i-lucide-sparkles'
  },
  {
    title: 'Тестовый заголовок',
    description: 'Мы то-то и то-то',
    icon: 'i-lucide-sparkles'
  },
]

const posts = [
  { 
    title: 'Nuxt Icon v1', 
    description: 'Discover Nuxt Icon v1!', 
    image: 'https://nuxt.com/assets/blog/nuxt-icon/cover.png', 
    date: '2024-11-25' 
  },
  { 
    title: 'Nuxt 3.14', 
    description: 'Nuxt 3.14 is out!', 
    image: 'https://nuxt.com/assets/blog/v3.14.png', 
    date: '2024-11-04' 
  },
  { 
    title: 'Nuxt 3.13', 
    description: 'Nuxt 3.13 is out!', 
    image: 'https://nuxt.com/assets/blog/v3.13.png', 
    date: '2024-08-22' 
  }
]

const FAQ_items = [
  {
    label: 'Icons',
    icon: 'i-lucide-smile',
    content: 'You have nothing to do, @nuxt/icon will handle it automatically.'
  },
  {
    label: 'Colors',
    icon: 'i-lucide-swatch-book',
    content: 'Choose a primary and a neutral color from your Tailwind CSS theme.'
  },
  {
    label: 'Components',
    icon: 'i-lucide-box',
    content: 'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
  },
  {
    label: 'Icons',
    icon: 'i-lucide-smile',
    content: 'You have nothing to do, @nuxt/icon will handle it automatically.'
  },
  {
    label: 'Icons',
    icon: 'i-lucide-smile',
    content: 'You have nothing to do, @nuxt/icon will handle it automatically.'
  }
]
</script>