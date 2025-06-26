import { Table } from './components/Table/Table';

const LOCAL_API = 'http://127.0.0.1:8000/voter_reg_deadlines/'

export default async function Page() {
  const response = await fetch(LOCAL_API);
  const data = await response.json();
  
  return (
    <main>
      <h1>VOTER REGISTRATION DEADLINES (2018)</h1>
      <Table data = {data}/>
    </main>
  );
}
