<template>
  <PageHeroElse
    title="Test"
    description="testtesttest"
    image="/images/office.png"
    image-alt="Office workspace"
  />
  <PageColumns
    title="Our Services"
    subtitle="Professional solutions tailored to your needs"
    :columns="[
      {
        icon: 'i-lucide-rocket',
        title: 'Web Development',
        description: 'Modern, responsive websites built with latest technologies.',
        buttonLabel: 'View Projects'
      },
      {
        icon: 'i-lucide-smartphone',
        title: 'Mobile Apps',
        description: 'Native and cross-platform mobile applications.',
        buttonLabel: 'Learn More',
        buttonLink: '/mobile'
      },
      {
        icon: 'i-lucide-cloud',
        title: 'Cloud Solutions',
        description: 'Scalable cloud infrastructure and deployment.'
      },
      {
        icon: 'i-lucide-cloud',
        title: 'Cloud Solutions',
        description: 'Scalable cloud infrastructure and deployment.'
      }

    ]"
    :columns-count="4"
  />
  
</template>