import axios from 'axios';

export const PostImage = async (data: any) => {
  return new Promise((resolve, reject) => {
    const form = new FormData();
    form.append("file", data);
    axios({
      method: "POST",
      url: "http://8.130.40.39:8000/upload-image",
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

