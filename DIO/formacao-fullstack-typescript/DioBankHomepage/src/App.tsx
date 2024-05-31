import Layout from './components/Layout/Layout.tsx'

import {
  Box,
  Center,
  Input,
  Button,
  Text,
  SimpleGrid,
} from '@chakra-ui/react'


function App() {

  return (
    <>
      <Layout>
        <Center>
          <Box minHeight="80vh" backgroundColor="whitesmoke" padding="2%" borderRadius="5%" margin="2%" width={"30%"}>
            <Center><Text fontSize='3xl'>Faça o Login</Text></Center>
            <SimpleGrid columns={1} spacing={10} padding="5%">
              <Center><Input placeholder='Email' width={"80%"} /></Center>
              <Center><Input placeholder='Senha' width={"80%"} /></Center>
              <Center><Button colorScheme='blue' bg={"blue.400"} width={"40%"}>Logar</Button></Center>
            </SimpleGrid>
          </Box>
        </Center>

      </Layout >
    </>
  )
}

export default App
