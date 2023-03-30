<template>
  <v-navigation-drawer
    v-model="toggle"
    fixed app>
    <v-toolbar flat dark :color="$root.themeColor" class="toolbar">
      <router-link :to="{ name: 'Dashboard' }">
        <img src="static/logo.png" width="36px"></img>
      </router-link>
      <router-link :to="{ name: 'Dashboard' }" class="text">
         SR Self Service Portal
      </router-link>
    </v-toolbar>
    <v-list>
      <v-list-tile exact active-class="active" :to="{name: 'Dashboard'}">
        <v-list-tile-action>
          <v-icon>dashboard</v-icon>
        </v-list-tile-action>
        <v-list-tile-title :class="['item-title']" >Dashboard</v-list-tile-title>
      </v-list-tile>
      <v-list-tile active-class="active" :to="{name: 'Ssh'}">
        <v-list-tile-action>
        <terminal-icon />
        </v-list-tile-action>
        <v-list-tile-title :class="['item-title' ]">SSH access</v-list-tile-title>
      </v-list-tile>
      <v-list-tile active-class="active" :to="{name: 'VpnAccess'}">
        <v-list-tile-action>
          <vpn-icon />
        </v-list-tile-action>
        <v-list-tile-title :class="['item-title' ]">VPN access</v-list-tile-title>
      </v-list-tile>
<!--      <v-list-tile active-class="active" :to="{name: 'WiFi'}">-->
<!--        <v-list-tile-action>-->
<!--          <wifi-icon />-->
<!--        </v-list-tile-action>-->
<!--        <v-list-tile-title :class="['item-title']">WIFI Krk</v-list-tile-title>-->
<!--      </v-list-tile>-->
      <v-list-tile active-class="active" :to="{name: 'MacAddress'}">
        <v-list-tile-action>
          <expansion-card-icon />
        </v-list-tile-action>
        <v-list-tile-title :class="['item-title']">Mac Address</v-list-tile-title>
      </v-list-tile>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  props: {
    toggle: {
        type: Boolean,
        required: false,
        default: true
    }
  },

  data() {
    return {
    }
  },
}
</script>

<style>
  .toolbar {
    font-weight: bold;
    font-size: 18px;
  }

  .toolbar .text {
    padding-left: 15px;
    color: white;
    text-decoration:none;
  }

  .item-title {
    font-size: 17px;
  }
  .item-sub-title {
    font-size: 15px;
    font-weight: 500;
  }
  .active {
    font-weight: bold !important;
  }
</style>
