<script setup lang="ts">
import { useRouter } from 'vue-router';
const router = useRouter();

</script>
<template>
    <v-app-bar color="#73beff" density="compact" style="position: fixed;">
        <v-btn icon="mdi-chevron-left" @click="router.back()"></v-btn>
        <v-app-bar-title>HITDetails帮助</v-app-bar-title>
        <v-spacer></v-spacer>
    </v-app-bar>
    <v-carousel style="margin-top: 0px;height: 100%;" hide-delimiters progress="primary" color="blue-lighten-1">
        <template v-slot:prev="{ props }">
            <v-btn variant="tonal" color="light-blue-darken-4" @click="props.onClick" icon="mdi-chevron-left"></v-btn>
        </template>
        <template v-slot:next="{ props }">
            <v-btn variant="tonal" color="light-blue-darken-4" @click="props.onClick" icon="mdi-chevron-right"></v-btn>
        </template>
        <v-carousel-item><v-img src="../assets/Intro1.png" alt="Intro" cover></v-img></v-carousel-item>
        <v-carousel-item><v-img src="../assets/Intro2.png" alt="Intro" cover></v-img></v-carousel-item>
        <v-carousel-item><v-img src="../assets/Intro3.png" alt="Intro" cover></v-img></v-carousel-item>
        <v-carousel-item><v-img src="../assets/Intro4.png" alt="Intro" cover></v-img></v-carousel-item>
        <v-carousel-item><v-img src="../assets/Intro5.png" alt="Intro" cover></v-img></v-carousel-item>
    </v-carousel>
</template>