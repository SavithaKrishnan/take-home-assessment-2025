"use client"
import { useState } from 'react'
import './table.css'


export type Data = {
    State: string
    Deadline_in_person: string
    Deadline_by_mail: string
    Deadline_online: string
    Election_day_registration: string
    Online_registration_link: string
    'Description': string
}[]

export type TableProps = {
  data: Data
}

// reformat column name (capitalize and remove underscore)
export const formatColName = (str: string) => str?.replaceAll('_', ' ').replace(/\b\w/g, substr => substr.toUpperCase())

export const Table = ({ data }: TableProps) => {
  const [sortedRows, setRows] = useState(data)
  const [order, setOrder] = useState('asc')
  const [sortKey, setSortKey] = useState(Object.keys(data[0])[0])

  // to filter rows
  const filter = (event: React.ChangeEvent<HTMLInputElement>) => {
    const value = event.target.value

    if (value) {
      setRows([ ...data.filter(row => {
        return Object.values(row)
          .join('')
          .toLowerCase()
          .includes(value)
      }) ])
    } else {
      setRows(data)
    }
  }

  // to sort rows 
  const sort = (value: keyof Data[0], order: string) => {
    const returnValue = order === 'desc' ? 1 : -1

    setSortKey(value)
    setRows([ ...sortedRows.sort((a, b) => {
      return a[value] > b[value]
        ? returnValue * -1
        : returnValue
    }) ])
  }

  // to determine asc/desc for sort
  const updateOrder = () => {
    const updatedOrder = order === 'asc' ? 'desc' : 'asc'

    setOrder(updatedOrder)
    sort(sortKey as keyof Data[0], updatedOrder)
  }

  return (
    <>
      <div className="controls">
        <input
          type="text"
          placeholder="Filter data..."
          onChange={filter}
        />
        <select onChange={(event) => sort(event.target.value as keyof Data[0], order)}>
          {Object.keys(data[0]).map((entry, index) => (
            <option value={entry} key={index}>
              Order by {formatColName(entry)}
            </option>
          ))}
        </select>
        <button onClick={updateOrder}>Switch order ({order})</button>
      </div>
      <table>
        <thead>
          <tr>
            {Object.keys(data[0]).map((entry, index) => (
              <th key={index}> {formatColName(entry)} </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {sortedRows.map((row, index) => (
            <tr key={index}>
              {Object.values(row).map((entry, columnIndex) => (
                <td key={columnIndex}>{entry}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
      {!sortedRows.length && (
        <h1>No results... Try expanding the search.</h1>
      )}
    </>
  )
}