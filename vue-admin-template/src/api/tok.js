import request from "@/utils/request";

export function show_token() {
  console.log("此处可以用showtoken")
  return request({

    url: '/api/show_token',
    method: 'GET'

  })
}
