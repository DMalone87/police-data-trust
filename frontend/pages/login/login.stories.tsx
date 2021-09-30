import React from "react"
import { Meta, Story } from "@storybook/react"
import UserLogin from "./"
import { AuthProvider } from "../../helpers"

export default {
  title: "Pages/Login",
  component: UserLogin,
  decorators: [
    (Story) => (
      <AuthProvider>
        <Story />
      </AuthProvider>
    )
  ]
} as Meta<typeof UserLogin>

const Template: Story<typeof UserLogin> = (args) => <UserLogin {...args} />

export const Default = Template.bind({})
Default.args = {
  
}