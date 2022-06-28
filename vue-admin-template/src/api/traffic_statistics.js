import request from "@/utils/request";

export function traffic_statistic(params) {
  console.log("here is traffic_statistic", params)
  return request({
    url: '/api/traffic_statistic/',
    method: 'post',
    data: params,
    headers: {
        'Content-Type': 'application/json'
      },
  })
}
