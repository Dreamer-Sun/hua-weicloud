import request from "@/utils/request";

export function deleteSite(params) {
  console.log("here is deleteSite", params)
  return request({
    url: '/api/delete_site/',
    method: 'post',
    data: params,
    headers: {
        'Content-Type': 'application/json'
      },
  })
}
