<script setup>
const { data: staffItems } = await useAsyncData('staff', () =>
  $fetch('http://localhost:8000/api/staff/'), { server: false }
)
</script>
<template>
    <PageHeroElse
        title="Test"
        description="testtesttest"
        image="/images/office.png"
        image-alt="Office workspace"
    />
    <StaffCard
        title="Наша команда"
        subtitle="Познакомьтесь с нашими сотрудниками"
        :items="staffItems ?? []"
    />
</template>

