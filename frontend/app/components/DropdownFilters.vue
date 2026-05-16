<template>
  <UDropdownMenu :items="menuItems" :ui="{ content: 'w-(--reka-dropdown-menu-trigger-width)' }" @update:open="isOpen = $event">
    <UButton
      :label="selectedItem?.name || label || field"
      :trailing-icon="isOpen ? 'i-lucide-chevron-up' : 'i-lucide-chevron-down'"
      color="neutral"
      variant="outline"
    />
  </UDropdownMenu>
</template>

<script setup>
const props = defineProps({
  field: {
    type: String,
    required: true,
  },
  label: {
    type: String,
    default: null,
  },
})

const emit = defineEmits(['change'])
const config = useRuntimeConfig()
const isOpen = ref(false)
const selectedItem = ref(null)

const { data: filterOptions } = await useAsyncData(
  `filters-${props.field}`,
  () => $fetch(`${config.public.apiBaseUrl}/api/vacancy-filters/${props.field}/`),
  { server: false }
)

const menuItems = computed(() => {
  const items = [
    { label: 'Все', onSelect: () => { selectedItem.value = null; emit('change', { field: props.field, value: null }) } },
  ]

  for (const option of (filterOptions.value ?? [])) {
    items.push({
      label: option.name,
      icon: selectedItem.value?.id === option.id ? 'i-lucide-check' : undefined,
      onSelect: () => { selectedItem.value = option; emit('change', { field: props.field, value: option.id }) },
    })
  }

  return [items]
})
</script>
