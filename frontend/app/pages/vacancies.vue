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
      :vacancies="vacanciesData ?? []"
    />

  </template>

<script setup>
const { data: vacanciesData } = await useAsyncData('vacancies-page', () =>
  $fetch('http://localhost:8000/api/vacancies/'), { server: false }
)
</script>