import request from "@/utils/request";

export function show_token() {
  return request({
    url: '/api/show_token',
    method: 'GET'
  })
}
