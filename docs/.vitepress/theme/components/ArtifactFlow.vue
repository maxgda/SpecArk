<template>
  <ol class="sa-flow">
    <li
      v-for="(step, i) in steps"
      :key="i"
      class="sa-flow__step"
      :class="{ 'is-last': i === steps.length - 1 }"
    >
      <span class="sa-flow__marker" aria-hidden="true">
        <span class="sa-flow__dot"></span>
      </span>
      <div class="sa-flow__content">
        <code class="sa-flow__file">{{ step.file }}</code>
        <p class="sa-flow__note">{{ step.note }}</p>
      </div>
    </li>
  </ol>
</template>

<script setup>
defineProps({
  steps: {
    type: Array,
    required: true
  }
});
</script>

<style scoped>
.sa-flow {
  list-style: none;
  padding: 0;
  margin: 18px 0 28px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  background: var(--vp-c-bg-soft);
}
.sa-flow__step {
  position: relative;
  display: flex;
  gap: 14px;
  padding: 16px 18px;
}
.sa-flow__step:not(:last-child) {
  border-bottom: 1px solid var(--vp-c-divider);
}
.sa-flow__marker {
  position: relative;
  flex-shrink: 0;
  width: 18px;
  display: flex;
  justify-content: center;
  padding-top: 6px;
}
.sa-flow__marker::before {
  content: "";
  position: absolute;
  top: 0;
  bottom: -16px;
  left: 50%;
  width: 2px;
  transform: translateX(-50%);
  background: linear-gradient(180deg, #d97757, #6e62c4);
  opacity: 0.45;
}
.sa-flow__step.is-last .sa-flow__marker::before {
  bottom: 50%;
}
.sa-flow__step:first-child .sa-flow__marker::before {
  top: 50%;
}
.sa-flow__dot {
  position: relative;
  z-index: 1;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: linear-gradient(135deg, #d97757, #6e62c4);
  box-shadow: 0 0 0 3px var(--vp-c-bg-soft);
}
.sa-flow__content {
  flex: 1;
  min-width: 0;
}
.sa-flow__file {
  display: inline-block;
  font-family: var(--vp-font-family-mono);
  font-size: 13px;
  padding: 2px 8px;
  border-radius: 6px;
  background: var(--vp-c-default-soft);
  color: var(--vp-c-text-1);
}
.sa-flow__note {
  margin: 6px 0 0;
  font-size: 14px;
  color: var(--vp-c-text-2);
  line-height: 1.55;
}
</style>
