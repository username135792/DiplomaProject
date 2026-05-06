<template>
  <UButton
    :label="label"
    :to="to"
    :color="color"
    :variant="variant"
    :size="size"
    :class="customClass"
    :icon="icon"
    :trailing-icon="trailingIcon"
    :block="block"
    :disabled="disabled"
    :loading="loading"
    :target="target"
  />
</template>

<script setup>
defineProps({
  label: {
    type: String,
    default: ''
  },
  to: {
    type: String,
    default: undefined
  },
  color: {
    type: String,
    default: 'primary'
  },
  variant: {
    type: String,
    default: 'solid'
  },
  size: {
    type: String,
    default: 'md'
  },
  customClass: {
    type: String,
    default: ''
  },
  icon: {
    type: String,
    default: undefined
  },
  trailingIcon: {
    type: String,
    default: undefined
  },
  block: {
    type: Boolean,
    default: false
  },
  disabled: {
    type: Boolean,
    default: false
  },
  loading: {
    type: Boolean,
    default: false
  },
  target: {
    type: String,
    default: undefined
  }
})
</script>
