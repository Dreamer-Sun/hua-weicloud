import request from "@/utils/request";

export function updateSite(params) {
  console.log("here is updateSite", params)
  return request({
    url: '/api/update_site/',
    method: 'post',
    data: params,
    headers: {
        'Content-Type': 'application/json'
      },
  })
}
