<template>
  <v-footer height="auto" dark :color="$root.themeColor" app>
    <v-flex class="text-xs-center">
        Devops Team - Smartrecruiters Inc. {{ year }}

    </v-flex>
  </v-footer>
</template>

<script>
export default {
  data() {
    return {
      year: new Date().getFullYear()
    }
  }
}
</script>

<style>

</style>
