<template>
  <PageHeroElse
      title="Наша команда"
      description="Познакомьтесь с нашей командой!"
      image="/images/office.png"
      image-alt="Office workspace"
  />

  <VacancyCards
      title="Последние вакансии"
      subtitle="Актуальные предложения от работодателей"
      :vacancies="vacanciesData ?? []"
    />
  </template>

<script setup>
import VacancyCards from '~/components/VacancyCards.vue';

const { data: vacanciesData } = await useAsyncData('vacancies-page', () =>
  $fetch('http://localhost:8000/api/vacancies/'), { server: false }
)
</script>