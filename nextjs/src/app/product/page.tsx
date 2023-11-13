import axiosInstance from '../../config/axios';
import axios from 'axios';

//import axios from 'axios';

async function getData() {

    try{const res = await axios.get('http://app/api/list-product-item')
    const data = res.data;

    if (!data) {
      console.log("Error: Failed to fetch data")
    }

    return data
  }catch (error) {
    //console.error("Error fetching data:", error);
    console.log("this works")
    return null;
  }
}

export default async function Home() {
  const fetchData = async () => {
    const data = await getData();


    if(data){
      console.log('Fetched data:', data);
    } else {
      console.log("Failed to fetch data !")
    }
  };

  fetchData();

  return (
    <main>
      <h1>My page</h1>
      <div>

      </div>

    </main>
  );
}

// "use client"

// import axiosInstance from '../../config/axios';
// export default async function Home() {
//   try {
//     const response = await axiosInstance.get('/api/list-product-item');
//     const data = await response.data;
//     console.log(data);
//   } catch (error) {
//     console.log(error);
//   }
//   return (
//     <div>
//       <h1>Home Page</h1>
//     </div>
//   )
// }


