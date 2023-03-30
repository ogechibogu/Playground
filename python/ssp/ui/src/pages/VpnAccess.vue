<template>
  <v-container grid-list-xl fluid>
    <v-snackbar v-model="showResult" :timeout="5000" v-bind:color="error === true ? 'error' : 'success'" top>{{ result }}</v-snackbar>
    <v-layout row>
      <v-flex xs8 sm4>
        <v-card class="mx-auto" outlined>
          <v-toolbar color="grey" dark>
            <v-toolbar-title>VPN Access</v-toolbar-title>
            <v-spacer></v-spacer>
          </v-toolbar>
          <v-list>
            <v-list-tile v-for="(item, index) in vpns" v-bind:key="index">
              <v-list-tile-avatar>
                <div>
                  <vpn-icon/>
                </div>
              </v-list-tile-avatar>
              <v-list-tile-content>
                <v-list-tile-title>
                  {{item}}
                </v-list-tile-title>
              </v-list-tile-content>
              <v-list-tile-action v-if="!notShowForVpn.includes(item)">
                <v-tooltip top>
                  <v-btn slot="activator" icon :loading="loadingButtons.includes(index)" @click="download(item, index)">
                    <v-icon>file_download</v-icon>
                  </v-btn>
                  Download configuration
                </v-tooltip>
              </v-list-tile-action>
            </v-list-tile>
            <v-list-tile v-if="vpns.length === 0">
              <v-list-tile-content :style="{'align-items':'center'}">
                No data available
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import client from "api-client";

export default {
  data() {
    return {
      error: true,
      showResult: false,
      result: '',
      vpns: [],
      loadingButtons: [],
      notShowForVpn: [],
    };
  },
  methods: {
    getVpnAccess() {
      client.fetchVpnAccess().then(response => {
        this.vpns = response.vpns;
      });
    },
    download(vpnName, index) {
      this.loadingButtons.push(index);
      client.fetchVpnConfig(vpnName)
        .then(response => {
          var fileURL = window.URL.createObjectURL(new Blob([response]));
          var fileLink = document.createElement('a');

          fileLink.href = fileURL;
          fileLink.setAttribute('download', vpnName.replace('access_', '') + '.ovpn');
          document.body.appendChild(fileLink);

          fileLink.click();
          this.loadingButtons.splice(this.loadingButtons.indexOf(index));
        })
        .catch(error => {
          this.loadingButtons.splice(this.loadingButtons.indexOf(index));
          this.result = error.msg;
          this.showResult = true;
          this.error = true;
        });
    }
  },
  created() {
    this.getVpnAccess();
  }
};
</script>
<style>
</style>
