import axios from 'axios';

export const PostImage = async (data: any) => {
  return new Promise((resolve, reject) => {
    const form = new FormData();
    form.append("file", data);
    axios({
      method: "POST",
      url: "http://116.204.83.124:9003/api/v1/upload",
      headers: {
        'Access-Control-Allow-Origin': '*',
        "Content-Type": "multipart/form-data",
        "Authorization": "Bearer 1|gFJ18bmuGg3LZOL6b9mpHJBrkzR5wIyq9f6h7a6F",
        "Accept": "application/json",
      },
      transformRequest: [function () {
        return form;
      }],
      data: form,
      params: form,
    })
    .then(res => {
      const url = res.data.data.links.url
      resolve(url);
    })
    .catch(err => {
      console.log(err);
      reject(err);
    });
  });
}

