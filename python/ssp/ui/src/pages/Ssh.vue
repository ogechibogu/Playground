<template>
  <v-container grid-list-xl fluid>
    <v-layout row>
      <v-flex xs8>
        <v-card>
          <v-card-text>
            <div class="pb-2 title font-weight-bold">What are we using ssh keys for ?</div>
            <v-spacer/>
            <div class="pb-1">1. Remote access to servers using ssh command to avoid typing password</div>
            <v-spacer></v-spacer>
            <div class="pb-1">2. Encrypt configuration/credentials that we send via email or jira ticket. (e.g. VPN configs)</div>
            <p class="pt-1 mb-0 green--text font-weight-bold subheading">TIP:</p>
            <p>- you can upload more than one key</p>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-snackbar v-model="showResult" :timeout="5000" v-bind:color="error === true ? 'error' : 'success'" top>{{ result }}</v-snackbar>
      <v-flex xs8>
        <v-card class="mx-auto" outlined>
          <v-toolbar color="grey" dark>
            <v-toolbar-title>SSH Public Keys</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-dialog
              v-model="dialog"
              width="700">
              <v-btn icon slot="activator">
                <v-icon medium>add</v-icon>
              </v-btn>
              <v-card>
                <v-card-title class="headline grey lighten-2" primary-title>
                  Add SSH public key
                </v-card-title>
                <v-card-text>
                  <div class="font-weight-bold">How to generate new ssh key:</div>
                  1. Open application "Terminal" on your Mac
                  <v-spacer/>
                  2. Paste there following code replacing "john.doe" with your "firstname.lastname"
                  <v-spacer></v-spacer>
                  <code>ssh-keygen -t rsa -b 4096 -m PEM -C "john.doe"</code>
                  <v-spacer/>
                  3. Press enter to accept all default settings
                  <v-spacer/>
                  4. Paste to Terminal: <code>cat ~/.ssh/id_rsa.pub</code>
                  <v-spacer/>
                  5. You should see a long string of text in Terminal starting with "ssh-rsa" end ending with your name, please copy it as a text and paste to
                  the field
                </v-card-text>
                <v-card-text>
                  <v-form>
                    <v-container>
                      <v-layout row wrap>
                        <v-textarea
                          v-model="addKeyForm.key"
                          :error="formError"
                          :rules="[rules.required, rules.validPublicKey]"
                          placeholder="paste ssh public key"></v-textarea>
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
            <v-list-tile v-for="(item, index) in keys" v-bind:key="index">
              <v-list-tile-avatar>
                <div>
                  <terminal-icon/>
                </div>
              </v-list-tile-avatar>
              <v-list-tile-content>
                <v-tooltip left>
                  <v-list-tile-title slot="activator">
                    {{item}}
                  </v-list-tile-title>
                  <span style="overflow-wrap: anywhere">{{item}}</span>
                </v-tooltip>
              </v-list-tile-content>
              <v-list-tile-action>
                <v-btn flat icon @click="removeKey(item)">
                  <v-icon color="red darken-2">remove_circle</v-icon>
                </v-btn>
              </v-list-tile-action>
            </v-list-tile>
            <v-list-tile v-if="keys.length === 0">
              <v-list-tile-content :style="{'align-items':'center'}">
                No data available
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex xs10 sm5>
        <ssh-permissions/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import client from "api-client";

export default {
  data() {
    return {
      keys: [],
      result: '',
      showResult: false,
      error: false,
      dialog: false,
      formError: false,
      addKeyForm: {
        key: ''
      },
      rules: {
        required: value => !!value || 'Required.',
        validPublicKey: value => !!value.match(/^ssh-rsa AAAA.*$/g) || "It doesn't look like ssh public key",
      },
    };
  },
  methods: {
    getKeys() {
      client.fetchPublicKeys().then(response => {
        this.keys = response.keys;
      });
    },
    removeKey(key) {
      client.removePublicKey(key)
        .then(() => {
          this.result = "Key removed";
          this.showResult = true;
          this.getKeys();
        })
        .catch((error) => {
          this.result = "Unable to remove key";
          this.showResult = true;
          this.error = true;
          this.getKeys();
        })
    },
    onCancel(event) {
      this.dialog = false;
      this.initForm();
    },
    onSubmit(event) {
      event.preventDefault();
      if (!this.addKeyForm.key) {
        this.formError = true;
      } else {
        this.addKey(this.addKeyForm);
      }
    },
    addKey(key) {
      client.addPublicKey(key)
        .then(() => {
          this.result = "New key added";
          this.showResult = true;
          this.dialog = false;
          this.initForm();
          this.getKeys();
        })
        .catch((error) => {
          this.result = "Error while adding key";
          this.showResult = true;
          this.error = true;
        })
    },
    initForm() {
      this.addKeyForm.key = '';
      this.formError = false
    },
  },
  created() {
    this.getKeys();
  }
};
</script>
<style>
</style>
