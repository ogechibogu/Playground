<template>
  <v-toolbar dark app :color="$root.themeColor">
    <v-toolbar-title>
      <v-toolbar-side-icon @click="toggleNavigationBar"></v-toolbar-side-icon>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-dialog v-model="dialogSettings" width="700">
      <v-card>
        <v-card-title class="headline" primary-title>Settings</v-card-title>
        <v-card-text>
          Change password
          <v-form>
            <v-container>
              <v-layout row wrap>
                <v-flex xs12 xs6 md1/>

                <v-flex xs12 sm6 md11>
                  <v-text-field
                    v-model="passwordForm.password"
                    :append-icon="showPassword ? 'visibility_off' : 'visibility'"
                    :type="showPassword ? 'text' : 'password'"
                    label="New Password"
                    hint="Please choose a complex one.."
                    :error="error"
                    :rules="[rules.validateLength]"
                    @click:append="showPassword = !showPassword"
                  />
                </v-flex>
                <v-flex xs12 sm6 md1/>
                <v-flex xs12 sm6 md11>
                  <v-text-field
                    v-model="passwordForm.passwordConfirm"
                    :append-icon="showPasswordConfirm ? 'visibility_off' : 'visibility'"
                    :type="showPasswordConfirm ? 'text' : 'password'"
                    label="Confirm New Password"
                    hint="and confirm it."
                    :error="error"
                    @click:append="showPasswordConfirm = !showPasswordConfirm"
                  />
                </v-flex>
              </v-layout>
            </v-container>
          </v-form>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" flat @click="cancelPasswordChange">Cancel</v-btn>
          <v-btn color="primary" flat @click="setUpSettings">Save Changes</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-snackbar v-model="showResult" :timeout="5000" v-bind:color="error === true ? 'error' : 'success'" top>{{ result }}</v-snackbar>

    <v-menu offset-y origin="center center" :nudge-bottom="10" transition="scale-transition">
      <v-btn icon large flat slot="activator" :ripple="false">
        <v-icon>account_box</v-icon>
      </v-btn>
      <v-list>
        <v-list-tile
          v-for="(item,index) in items"
          :key="index"
          :to="!item.href ? { name: item.name } : null"
          :href="item.href"
          ripple="ripple"
          :disabled="item.disabled"
          :target="item.target"
          @click="item.click"
        >
          <v-list-tile-action v-if="item.icon">
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-menu>
  </v-toolbar>
</template>
<script>
import {AUTH_LOGOUT, AUTH_REQUEST} from "actions/auth";
import client from "api-client";

export default {
  data() {
    return {
      rating: null,
      dialog: false,
      dialogSettings: false,
      showPassword: null,
      showPasswordConfirm: null,
      passwordForm: {
        password: '',
        passwordConfirm: '',
      },
      error: false,
      showResult: false,
      result: "",
      rules: {
        validateLength: value => value.length >= 12 || 'Password require at least 12 char',
      },
      items: [
        {
          icon: "settings",
          href: "#",
          title: "Settings",
          click: () => {
            const vm = this;

            vm.dialogSettings = true;
          }
        },
        {
          icon: "exit_to_app",
          href: "#",
          title: "Log Out",
          click: () => {
            this.logout()

          }
        }
      ]

    };
  },
  methods: {
    logout: function () {
      this.$store.dispatch(AUTH_LOGOUT).then(() => this.$router.push('/login'))
    },

    toggleNavigationBar() {
      const vm = this;

      vm.$emit("toggleNavigationBar");
    },

    setUpSettings() {
      const vm = this;
      var store = this.$store;

      if (vm.passwordForm.password.length === 0 || vm.passwordForm.passwordConfirm.length === 0) {
        vm.result = "Password can't be null.";
        vm.showResult = true;
        vm.error = true;
        return;
      }

      if (vm.passwordForm.password !== vm.passwordForm.passwordConfirm) {
        vm.error = true;
        vm.result = "Passwords does not match the confirm password.";
        vm.showResult = true;
        return;
      }

      client.changePassword(vm.passwordForm)
        .then(response => {
          vm.result = "Password changed succesfully.";
          vm.error = false;
          vm.showResult = true;
          vm.dialogSettings = false;
          let username = store.state.user.profile.uid.shift();
          store.dispatch(AUTH_REQUEST, {"username": username, "password": vm.passwordForm.password});
          this.initForm()
        })
        .catch(error => {
          vm.result = "Password not changed";
          vm.error = true;
          vm.showResult = true;
          this.initForm();
        })
    },

    initForm() {
      this.passwordForm.password = '';
      this.passwordForm.passwordConfirm = '';
    },

    cancelPasswordChange() {
      this.dialogSettings = false;
      this.initForm();
    }
  }
};
</script>
