<template>
  <PageHeroElse
    title="Test"
    description="testtesttest"
    image="/images/office.png"
    image-alt="Office workspace"
  />
  <NewsPageList
    title="Latest News"
    subtitle="Stay updated with our latest announcements and articles"
    :items="[
      {
        title: 'New Product Launch',
        description: 'We are excited to announce our latest product that revolutionizes the industry.',
        photo: '/images/news/product-launch.jpg',
        photoAlt: 'New product showcase',
        meta: [
          { icon: 'i-lucide-calendar', text: 'April 3, 2026' },
          { icon: 'i-lucide-user', text: 'John Doe' }
        ],
        buttonLabel: 'Read More',
        buttonLink: '/news/product-launch'
      },
      {
        title: 'Company Milestone',
        description: 'We have reached 10,000 happy customers worldwide.',
        photo: '/images/news/milestone.jpg',
        photoCaption: 'Celebrating our achievement'
      }
    ]"
    :divide="true"
  />
  </template>