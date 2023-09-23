import { Tabs, Tab, Container } from "react-bootstrap";
import { ProductsTableContainer } from "../ProductsTable/ProductsTableContainer";
import { CreateProduct } from "../ProductForms/CreateProduct/CreateProduct";

export const MainPage = () => {
  const tabsItems = [
    {
      id: "productsTable",
      component: <ProductsTableContainer />,
      title: "Tabela de Produtos",
    },
    {
      id: "productsForm",
      component: <CreateProduct />,
      title: "Cadastro de Novos Produtos",
    },
    {
      id: "storesForm",
      component: <div>bb</div>,
      title: "Cadastro de Novas Lojas",
    },
  ];
  return (
    <Container>

    <Tabs defaultActiveKey="tabItem.title" id="tabs" className="mb-3">
      {tabsItems.map((tabItem) => (
        <Tab title={tabItem.title} eventKey={tabItem.id} key={tabItem.id}>
          {tabItem.component}
        </Tab>
      ))}
      {/* <Tab title={"tabItem.title"} eventKey={"tabItem.id"} key={"tabItem.id"}>
        <div>aaa</div>
        </Tab>
        
        <Tab
        title={"tabItem.title 2"}
        eventKey={"tabItem.id2"}
        key={"tabItem.id2"}
        >
        <div>bbb</div>
      </Tab> */}
    </Tabs>
      </Container>
  );
};
