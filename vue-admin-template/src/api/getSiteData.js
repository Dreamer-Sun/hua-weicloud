import request from "@/utils/request";

export function getSiteData() {
  console.log("此处可以用getSite")
  return request({
    url: '/api/getSiteData',
    method: 'GET'
  })
}
