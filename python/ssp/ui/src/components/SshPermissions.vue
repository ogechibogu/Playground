<template>
  <div>
    <v-toolbar color="grey" dark>
      <v-toolbar-title>SSH Permissions</v-toolbar-title>
    </v-toolbar>
    <v-data-table
      class="table"
      :headers="headers"
      :items="permissions"
      hide-actions>
      <template slot="items" slot-scope="props">
        <td class="text-xs-left">{{ props.item.name }}</td>
        <td class="text-xs-left">{{ props.item.expire }}</td>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import client from "api-client";

export default {
  data() {
    return {
      permissions: [],
      headers: [
        {
          text: 'Name',
          value: 'name',
          align: 'left',
          sortable: true
        },
        {
          text: 'Expire',
          value: 'expire',
          align: 'left',
          sortable: true
        }
      ]
    }
  },

  methods: {
    getPermissions() {
      client.fetchSshPermissions().then(response => {
        this.permissions = response.permissions
      }).catch(() => {
        this.permissions = []
      })
    }
  },

  created() {
    this.getPermissions();
  }
}
</script>

<style>
  .table {
    border-radius: 3px;
    background-clip: border-box;
    border: 1px solid rgba(0, 0, 0, 0.125);
    box-shadow: 1px 1px 1px 1px rgba(0, 0, 0, 0.21);
    background-color: transparent;
  }
</style>
