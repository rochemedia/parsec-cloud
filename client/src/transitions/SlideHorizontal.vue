<!-- Parsec Cloud (https://parsec.cloud) Copyright (c) BUSL-1.1 2016-present Scille SAS -->
<template>
  <transition-group :name="!props.reverseDirection ? 'slide-left' : 'slide-right'">
    <slot />
  </transition-group>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';

const props = defineProps<{
  reverseDirection?: boolean
}>();
</script>

<style scoped>
.slide-left-enter-active, .slide-right-enter-active {
  transition: 0.4s ease-in-out;
  transition-delay: 0.4s;
}

.slide-left-leave-active, .slide-right-leave-active {
  transition: 0.4s;
}

.slide-left-enter-from, .slide-right-leave-to {
  opacity: 0;
  transform: translate(-100%, 0);
}

.slide-left-leave-to, .slide-right-enter-from {
  opacity: 0;
  transform: translate(100%, 0);
}
</style>
