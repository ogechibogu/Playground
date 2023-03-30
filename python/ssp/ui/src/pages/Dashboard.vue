<template>
  <v-container fluid grid-list-xl>
    <v-layout row wrap>
      <v-flex xs6 sm3>
        <v-text-field v-bind:value="user.displayName" label="Display Name" readonly></v-text-field>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs6 sm3>
        <v-text-field v-bind:value="user.givenName" label="Name" readonly></v-text-field>
      </v-flex>
      <v-flex xs6 sm3>
        <v-text-field v-bind:value="user.sn" label="Surname" readonly></v-text-field>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs6 sm3>
        <v-text-field v-bind:value="user.mail" label="E-mail" readonly></v-text-field>
      </v-flex>
      <v-flex xs6 sm3>
        <v-text-field v-bind:value="user.uidNumber" label="Uid Number" readonly></v-text-field>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import {mapState} from "vuex";
import {USER_REQUEST} from 'actions/user'

export default {
  computed: mapState({ user: state => state.user.profile}),
  created: function() {
    if (this.$store.getters.isAuthenticated && this.$store.state.user.status !== 'loading') {
      this.$store.dispatch(USER_REQUEST);
    }
  }
}
</script>

<style>

</style>
