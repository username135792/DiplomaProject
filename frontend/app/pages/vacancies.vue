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

const config = useRuntimeConfig()
const { data: vacanciesData } = await useAsyncData('vacancies-page', () =>
  $fetch(`${config.public.apiBaseUrl}/api/vacancies/`), { server: false }
)
</script>