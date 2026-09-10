<script setup>
import { onBeforeUnmount, onMounted, ref } from "vue";

const props = defineProps({
  services: {
    type: Array,
    default: () => [
      { id: "accounts-daemon.service", enabled: true },
      { id: "apache2.service", enabled: false },
      { id: "cron.service", enabled: true },
      { id: "ssh.service", enabled: true },
    ],
  },
});

const emit = defineEmits(["accept", "cancel"]);
const dialog = ref(null);
const selected = ref(new Set(props.services.filter((service) => service.enabled).map((service) => service.id)));

function handleEscape() {
  emit("cancel");
}

function toggleService(serviceId, checked) {
  const next = new Set(selected.value);
  if (checked) next.add(serviceId);
  else next.delete(serviceId);
  selected.value = next;
}

function accept() {
  emit(
    "accept",
    props.services.filter((service) => selected.value.has(service.id)).map((service) => service.id),
  );
}

onMounted(() => dialog.value?.addEventListener("tui:escape", handleEscape));
onBeforeUnmount(() => dialog.value?.removeEventListener("tui:escape", handleEscape));
</script>

<template>
  <!--
    Consumption recipe only. The host Vue application loads vendored
    web-tui-kit/tokens.css, tui.css, and optionally tui.js once globally.
  -->
  <main class="tui-screen">
    <section
      ref="dialog"
      class="tui-dialog"
      data-tui-escape-close
      aria-labelledby="package-title"
    >
      <h1 id="package-title" class="tui-dialog-title">Package configuration</h1>

      <p class="tui-dialog-copy">Daemons using outdated libraries</p>
      <p class="tui-dialog-copy">Which services should be restarted?</p>

      <div
        class="tui-checklist"
        data-tui-list
        role="group"
        aria-label="Services to restart"
      >
        <label v-for="(service, index) in services" :key="service.id" class="tui-check-row">
          <input
            type="checkbox"
            :checked="selected.has(service.id)"
            :autofocus="index === 0"
            @change="toggleService(service.id, $event.target.checked)"
          >
          <span class="tui-mark" aria-hidden="true"></span>
          <span>{{ service.id }}</span>
          <span class="tui-help">&lt;Help&gt;</span>
        </label>
      </div>

      <div class="tui-actions">
        <button class="tui-button" type="button" accesskey="o" @click="accept">
          <span class="tui-hotkey">O</span>k
        </button>
      </div>
    </section>
  </main>
</template>
