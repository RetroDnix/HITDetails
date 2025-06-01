<script setup lang = "ts">
import DefaultBar from '@/components/NavigationBar.vue'
</script>
<template>
  <v-app>
    <v-layout style="overflow: hidden;">
      <DefaultBar />
      <v-main>
        <div class="mainContainer">
          <router-view />
        </div>
      </v-main>
    </v-layout>
  </v-app>
</template>
<style>
.mainContainer {
  position: static;
  overflow-y: hidden;
}
</style>
