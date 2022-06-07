import request from "@/utils/request";

export function getSiteData() {
  return request({
    url: '/api/getsite_Data',
    method: 'GET'
  })
}
