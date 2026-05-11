<template>
  <div class="sa-terminal">
    <div class="sa-terminal__bar">
      <span class="sa-terminal__dot sa-dot-red"></span>
      <span class="sa-terminal__dot sa-dot-yellow"></span>
      <span class="sa-terminal__dot sa-dot-green"></span>
      <span class="sa-terminal__title">{{ title }}</span>
    </div>
    <div class="sa-terminal__body">
      <slot />
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    default: "terminal"
  }
});
</script>

<style scoped>
.sa-terminal {
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
  margin: 18px 0 28px;
}
.sa-terminal__bar {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 14px;
  background: linear-gradient(180deg, rgba(0, 0, 0, 0.04), rgba(0, 0, 0, 0.02));
  border-bottom: 1px solid var(--vp-c-divider);
}
.dark .sa-terminal__bar {
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.04), rgba(255, 255, 255, 0.02));
}
.sa-terminal__dot {
  display: inline-block;
  width: 11px;
  height: 11px;
  border-radius: 50%;
}
.sa-dot-red    { background: #ff5f56; }
.sa-dot-yellow { background: #ffbd2e; }
.sa-dot-green  { background: #27c93f; }
.sa-terminal__title {
  margin-left: 8px;
  font-size: 12px;
  font-weight: 500;
  color: var(--vp-c-text-2);
  font-family: var(--vp-font-family-mono);
  letter-spacing: 0.02em;
}
.sa-terminal__body {
  padding: 4px 6px 6px;
}
.sa-terminal__body :deep(div[class*="language-"]) {
  margin: 8px 0;
  border-radius: 8px;
}
.sa-terminal__body :deep(div[class*="language-"]:first-child) {
  margin-top: 8px;
}
.sa-terminal__body :deep(div[class*="language-"]:last-child) {
  margin-bottom: 8px;
}
</style>
