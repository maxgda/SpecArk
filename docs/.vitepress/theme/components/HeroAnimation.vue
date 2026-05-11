<template>
  <div class="hero-anim" aria-hidden="true">
    <svg viewBox="0 0 320 320" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="haGrad" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="#d97757" />
          <stop offset="100%" stop-color="#6e62c4" />
        </linearGradient>
        <radialGradient id="haGlow" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#d97757" stop-opacity="0.35" />
          <stop offset="100%" stop-color="#6e62c4" stop-opacity="0" />
        </radialGradient>
      </defs>

      <circle class="ha-glow" cx="160" cy="160" r="140" fill="url(#haGlow)" />

      <g class="ha-ring ha-ring-1">
        <circle cx="160" cy="160" r="110" fill="none" stroke="url(#haGrad)" stroke-width="1.25" stroke-dasharray="3 7" opacity="0.55" />
      </g>
      <g class="ha-ring ha-ring-2">
        <circle cx="160" cy="160" r="78" fill="none" stroke="url(#haGrad)" stroke-width="1" stroke-dasharray="2 6" opacity="0.5" />
      </g>

      <g class="ha-core">
        <rect x="130" y="130" width="60" height="60" rx="10" fill="url(#haGrad)" />
        <rect x="138" y="142" width="44" height="3" rx="1.5" fill="white" opacity="0.85" />
        <rect x="138" y="152" width="34" height="3" rx="1.5" fill="white" opacity="0.7" />
        <rect x="138" y="162" width="38" height="3" rx="1.5" fill="white" opacity="0.7" />
        <rect x="138" y="172" width="28" height="3" rx="1.5" fill="white" opacity="0.55" />
      </g>

      <g class="ha-tokens">
        <g class="ha-token ha-token-1">
          <rect x="-14" y="-12" width="28" height="24" rx="5" fill="#d97757" />
          <rect x="-9" y="-7" width="18" height="2" rx="1" fill="white" opacity="0.85" />
          <rect x="-9" y="-2" width="14" height="2" rx="1" fill="white" opacity="0.7" />
          <rect x="-9" y="3" width="16" height="2" rx="1" fill="white" opacity="0.7" />
        </g>
        <g class="ha-token ha-token-2">
          <rect x="-14" y="-12" width="28" height="24" rx="5" fill="#a36c8d" />
          <rect x="-9" y="-7" width="18" height="2" rx="1" fill="white" opacity="0.85" />
          <rect x="-9" y="-2" width="14" height="2" rx="1" fill="white" opacity="0.7" />
          <rect x="-9" y="3" width="16" height="2" rx="1" fill="white" opacity="0.7" />
        </g>
        <g class="ha-token ha-token-3">
          <rect x="-14" y="-12" width="28" height="24" rx="5" fill="#6e62c4" />
          <rect x="-9" y="-7" width="18" height="2" rx="1" fill="white" opacity="0.85" />
          <rect x="-9" y="-2" width="14" height="2" rx="1" fill="white" opacity="0.7" />
          <rect x="-9" y="3" width="16" height="2" rx="1" fill="white" opacity="0.7" />
        </g>
      </g>
    </svg>
  </div>
</template>

<style scoped>
.hero-anim {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.hero-anim svg {
  width: 100%;
  height: 100%;
  overflow: visible;
}

.ha-glow {
  animation: ha-pulse 6s ease-in-out infinite;
  transform-origin: 160px 160px;
}

.ha-ring {
  transform-origin: 160px 160px;
}
.ha-ring-1 { animation: ha-spin 28s linear infinite; }
.ha-ring-2 { animation: ha-spin-rev 22s linear infinite; }

.ha-core {
  transform-origin: 160px 160px;
  animation: ha-bob 5s ease-in-out infinite;
}

.ha-token {
  transform-origin: 0 0;
}
.ha-token-1 {
  transform: translate(270px, 160px);
  animation: ha-orbit-1 18s linear infinite;
}
.ha-token-2 {
  transform: translate(160px, 50px);
  animation: ha-orbit-2 18s linear infinite;
}
.ha-token-3 {
  transform: translate(50px, 160px);
  animation: ha-orbit-3 18s linear infinite;
}

@keyframes ha-spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
@keyframes ha-spin-rev {
  from { transform: rotate(360deg); }
  to { transform: rotate(0deg); }
}
@keyframes ha-pulse {
  0%, 100% { transform: scale(1); opacity: 0.85; }
  50% { transform: scale(1.08); opacity: 1; }
}
@keyframes ha-bob {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-4px); }
}
@keyframes ha-orbit-1 {
  0%   { transform: translate(160px, 160px) rotate(0deg)   translate(110px) rotate(0deg); }
  100% { transform: translate(160px, 160px) rotate(360deg) translate(110px) rotate(-360deg); }
}
@keyframes ha-orbit-2 {
  0%   { transform: translate(160px, 160px) rotate(120deg) translate(110px) rotate(-120deg); }
  100% { transform: translate(160px, 160px) rotate(480deg) translate(110px) rotate(-480deg); }
}
@keyframes ha-orbit-3 {
  0%   { transform: translate(160px, 160px) rotate(240deg) translate(110px) rotate(-240deg); }
  100% { transform: translate(160px, 160px) rotate(600deg) translate(110px) rotate(-600deg); }
}

@media (max-width: 640px) {
  .hero-anim,
  .hero-anim svg {
    overflow: hidden;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ha-glow,
  .ha-ring-1,
  .ha-ring-2,
  .ha-core,
  .ha-token-1,
  .ha-token-2,
  .ha-token-3 {
    animation: none;
  }
}
</style>
