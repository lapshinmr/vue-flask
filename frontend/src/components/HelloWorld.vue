<template>
  <v-container>
    <v-row class="text-center">
      <v-col>
        {{ msg }}
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: ['msg'],
  data: () => ({
  })
}
</script>
