<template>
  <PageHeroElse
    title="Наша команда"
    description="Познакомьтесь с нашей командой!"
    image="/images/office.png"
    image-alt="Office workspace"
  />
  <Testimonial
    image="/images/PutinTestimonial.jpg"   
    quote="Любой гражданин, который хотел бы стать муниципальным или госслужащим, должен понимать, что вступление в должность связано с жесткими антикоррупционными требованиями, с определенными ограничениями, которые человек обязан строго соблюдать"
    alt="Customer photo"
    author='Владимир Владимирович Путин'
  />
  <NewsPageList
    title="Latest News"
    subtitle="Stay updated with our latest announcements"
    :items="[
      {
        title: 'New Product Launch',
        description: 'Да, полностью и без попыток уволить. В отличие от частного бизнеса, где длительный больничный — частая причина для сокращения или давления с просьбой «уйти по собственному», госслужащий защищен законом. Вам оплатят весь период нетрудоспособности, а ваше рабочее место сохранится. Более того, после выхода на работу вас не могут понизить в должности или чине из-за болезни.',
        image: '/images/office.png',
        imageAlt: 'New product showcase'
      },
      {
        title: 'Company Expansion',
        description: 'We are opening new offices in three cities...',
        image: '/images/office.png'
      },
      {
        title: 'Company Expansion',
        description: 'We are opening new offices in three cities...',
        image: '/images/office.png'
      }
    ]"
  />
</template>
