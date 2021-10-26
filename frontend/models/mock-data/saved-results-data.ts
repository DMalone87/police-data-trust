import { IncidentTableData, incidentsColumns, formatDate } from "../incidents"

// SAVED RESULTS DATA TABLE
export interface SavedResultsType extends IncidentTableData {
  searchDate: number // UNIX timestamp
}

export const resultsColumns = [
  {
    Header: "Search Date",
    accessor: (row: any) => formatDate(row["searchDate"]),
    id: "searchDate"
  },
  ...incidentsColumns
]

// OLD FORMAT - here to avoid breaking existing components
export const savedResultsData = [
  {
    searchDate: "2021/09/07",
    dates: "2003/01/01",
    incidentType: "Use of force",
    officersInvolved: ["Dan Smith"],
    subject: "unknown",
    source: "News Article",
    recordId: 1
  },
  {
    searchDate: "2021/09/07",
    dates: "2003/01/01",
    incidentType: "Use of force",
    officersInvolved: ["John Smith"],
    subject: "unknown",
    source: "News Article",
    recordId: 2
  },
  {
    searchDate: "2021/09/07",
    dates: "2003/01/01",
    incidentType: "Use of force",
    officersInvolved: ["Ed Smith, Vince Gilligan"],
    subject: "unknown",
    source: "News Article",
    recordId: 3
  },
  {
    searchDate: "2021/09/07",
    dates: "2003/01/01",
    incidentType: "Use of force",
    officersInvolved: ["John Smith"],
    subject: "unknown",
    source: "News Article",
    recordId: 4
  },
  {
    searchDate: "2021/09/07",
    dates: "2003/01/01",
    incidentType: "Use of force",
    officersInvolved: ["John Smith"],
    subject: "unknown",
    source: "News Article",
    recordId: 5
  },
  {
    searchDate: "2021/09/07",
    dates: "2003/01/01",
    incidentType: "Use of force",
    officersInvolved: ["John Smith"],
    subject: "unknown",
    source: "News Article",
    recordId: 6
  },
  {
    searchDate: "2021/09/07",
    dates: "2003/01/01",
    incidentType: "Use of force",
    officersInvolved: ["John Smith"],
    subject: "unknown",
    source: "News Article",
    recordId: 7
  },
  {
    searchDate: "2021/09/07",
    dates: "2003/01/01",
    incidentType: "Use of force",
    officersInvolved: ["Dan Smith"],
    subject: "unknown",
    source: "News Article",
    recordId: 8
  },
  {
    searchDate: "2021/09/07",
    dates: "2003/01/01",
    incidentType: "Use of force",
    officersInvolved: ["John Smith"],
    subject: "unknown",
    source: "News Article",
    recordId: 9
  },
  {
    searchDate: "2021/09/07",
    dates: "2003/01/01",
    incidentType: "Use of force",
    officersInvolved: ["Ed Smith, Vince Gilligan"],
    subject: "unknown",
    source: "News Article",
    recordId: 10
  },
  {
    searchDate: "2021/09/07",
    dates: "2003/01/01",
    incidentType: "Use of force",
    officersInvolved: ["John Smith"],
    subject: "unknown",
    source: "News Article",
    recordId: 11
  }
]
