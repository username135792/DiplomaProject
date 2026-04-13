<template>
  <PageHeroElse
      title="Наша команда"
      description="Познакомьтесь с нашей командой!"
      image="/images/office.png"
      image-alt="Office workspace"
  />

  <LatestVacancies
      title="Последние вакансии"
      subtitle="Актуальные предложения от работодателей"
      :vacancies="vacanciesData"
    />

  </template>

<script setup>
const vacanciesData = [
  {
    title: 'Frontend Developer (Vue.js/Nuxt)',
    company: 'Отдел информационного развития',
    location: 'Сургут, ул. Энергетиков, 22',
    salary: 'от 150 000 ₽',
    employmentType: 'Полная занятость',
    experience: '1-3 года',
    isNew: true,
    skills: ['Vue.js', 'Nuxt', 'TypeScript', 'TailwindCSS'],
    detailsLink: '/vacancies/1'
  },
  {
    title: 'Frontend Developer (Vue.js/Nuxt)',
    company: 'Отдел управления кадров и наград',
    location: 'Сургут, ул. Энергетиков, 22',
    salary: 'от 150 000 ₽',
    employmentType: 'Полная занятость',
    experience: '1-3 года',
    isNew: true,
    skills: ['Высшее образование', 'Работа с потенциальными сотрудниками'],
    detailsLink: '/vacancies/2'
  }
]
</script>