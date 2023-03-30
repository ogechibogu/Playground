<template>
  <v-container grid-list-xl fluid>
    <v-snackbar v-model="showResult" :timeout="5000" v-bind:color="error === true ? 'error' : 'success'" top>{{ result }}</v-snackbar>
    <v-dialog v-model="showHelp" fullscreen hide-overlay transition="dialog-bottom-transition">
      <v-card>
        <v-toolbar dark color="grey">
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn dark flat @click="showHelp = false">
              <v-icon>close</v-icon>
            </v-btn>
          </v-toolbar-items>
        </v-toolbar>
        <v-layout row>
          <v-flex offset-xs3 xs5>
            <v-card>
              <v-card-text>
                <v-img src="static/step_1.png"></v-img>
              </v-card-text>
              <v-card-text>
                <v-img src="static/step_2.png"></v-img>
              </v-card-text>
              <v-card-text>
                <v-img src="static/step_3.png"></v-img>
              </v-card-text>
            </v-card>
          </v-flex>

        </v-layout>
      </v-card>
    </v-dialog>
    <v-layout row>
      <v-flex xs8>
        <v-card>
          <v-card-text>
            <p>Wired and WiFi Secure network is restricted to registered devices by physical (MAC) address.</p>
            <p>If you need help how to find your mac address check <a @click="showHelp = true">HERE</a></p>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex xs8 sm4>
        <v-card class="mx-auto" outlined>
          <v-toolbar color="grey" dark>
            <v-toolbar-title>Mac Addresses</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-dialog
              v-model="dialog"
              width="700">
              <v-btn icon slot="activator">
                <v-icon medium>add</v-icon>
              </v-btn>
              <v-card>
                <v-card-title class="headline grey lighten-2" primary-title>
                  Add Mac Address
                </v-card-title>
                <v-card-text>
                  <v-form>
                    <v-container>
                      <v-layout row wrap>
                        <v-text-field
                          v-model="addAddressForm.address"
                          :error="formError"
                          :rules="[rules.required, rules.validMacAddress]"
                          placeholder="01:23:45:67:89:AB"></v-text-field>
                      </v-layout>
                    </v-container>
                  </v-form>
                </v-card-text>
                <v-divider></v-divider>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="primary" flat @click="onCancel"> Cancel</v-btn>
                  <v-btn color="primary" flat @click="onSubmit">Submit</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-toolbar>
          <v-list two-line>
            <v-list-tile v-for="(item, index) in addresses" v-bind:key="index">
              <v-list-tile-avatar>
                <div>
                  <expansion-card-icon/>
                </div>
              </v-list-tile-avatar>
              <v-list-tile-content>
                <v-list-tile-title>
                  {{item}}
                </v-list-tile-title>
              </v-list-tile-content>
              <v-list-tile-action>
                <v-btn flat icon @click="removeAddress(item)">
                  <v-icon color="red darken-2">remove_circle</v-icon>
                </v-btn>
              </v-list-tile-action>
            </v-list-tile>
            <v-list-tile v-if="addresses.length === 0">
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
      addresses: [],
      result: '',
      showResult: false,
      error: false,
      dialog: false,
      formError: false,
      showHelp: false,
      addAddressForm: {
        address: ''
      },
      rules: {
        required: value => !!value || 'Required.',
        validMacAddress: value => !!value.match(/^((([a-fA-F0-9][a-fA-F0-9]+[:]){5})([a-fA-F0-9][a-fA-F0-9])$)/g) || 'Invalid Mac Address',
      },
    };
  },
  methods: {
    getAddresses() {
      client.fetchMacAddresses().then(response => {
        this.addresses = response.addresses;
      });
    },
    removeAddress(address) {
      client.removeMacAddress(address)
        .then(() => {
          this.result = "Address removed";
          this.showResult = true;
          this.getAddresses();
        })
        .catch((error) => {
          this.result = error.msg;
          this.showResult = true;
          this.error = true;
          this.getAddresses();
        })
    },
    onCancel(event) {
      this.dialog = false;
      this.initForm();
    },
    onSubmit(event) {
      event.preventDefault();
      if (!this.addAddressForm.address) {
        this.formError = true;
      } else {
        this.addAddress(this.addAddressForm);
      }
    },
    addAddress(addressForm) {
      client.addMacAddress(addressForm)
        .then(() => {
          this.result = "New address added";
          this.showResult = true;
          this.dialog = false;
          this.initForm();
          this.getAddresses();
        })
        .catch((error) => {
          this.result = error.msg;
          this.showResult = true;
          this.error = true;
        })
    },
    initForm() {
      this.addAddressForm.address = '';
      this.formError = false
    },
  },
  created() {
    this.getAddresses();
  }
};
</script>
<style>
</style>
