<template>
  <v-container grid-list-xl fluid>
    <v-layout row>
      <v-flex xs8>
        <v-card color="white">
          <v-card-text>
            <v-card-text>
              <p class="title font-weight-bold">CAUTION !!!</p>
              <p class="subheading">If you are in Kraków Office please use wired connection as much as possible,
              save WiFi resources for people who can't use wired connection.
              </p>
            </v-card-text>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex xs8>
        <v-card color="white">
          <v-card-text>
            <div class="subheading font-weight-bold">Access to WiFi secure is provided with the same credentials as this portal.</div>
          </v-card-text>
          <v-card-text>
            Make sure your MAC Address is present <a @click="$router.push({ name: 'MacAddress' })">HERE</a>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {

}
</script>
<style>
</style>
