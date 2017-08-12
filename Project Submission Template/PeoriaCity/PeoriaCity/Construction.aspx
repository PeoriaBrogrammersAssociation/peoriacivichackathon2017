<%@ Page Title="WAZE LINK" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Construction.aspx.cs" Inherits="PeoriaCity.Construction" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <h2><%: Title %></h2>
    <%-- <h3>Waze Link</h3>--%>
    <br />
    <br />

    <asp:Label ID="Label1" runat="server" Text="Event Type"></asp:Label>
    <asp:DropDownList ID="DropDownList1" runat="server">
        <asp:ListItem Selected="True">Select Event Type</asp:ListItem>
        <asp:ListItem>Road Construction</asp:ListItem>
        <asp:ListItem>Road Blockage</asp:ListItem>
    </asp:DropDownList>
    &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <asp:Label ID="Label2" runat="server" Text="Name of event"></asp:Label>
    <asp:DropDownList ID="DropDownList2" runat="server">
         <asp:ListItem Selected="True">Select Name of Event</asp:ListItem>
        <asp:ListItem>Madison Ave constuction</asp:ListItem>
        <asp:ListItem>Alta Rd constuction</asp:ListItem>
        <asp:ListItem>Taste of Peoria</asp:ListItem>
        <asp:ListItem>Musical Festival</asp:ListItem>
    </asp:DropDownList>
    <br />
    <br />
    <br />
    From Street
    <asp:TextBox ID="txtStreetFrom" runat="server" Width="299px"></asp:TextBox>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    To Street&nbsp;
    <asp:TextBox ID="txtStreetTo" runat="server" Width="299px"></asp:TextBox>
    <br />

    <br />
    <br />
    Longitude&nbsp;&nbsp;
    <asp:TextBox ID="txtLng" runat="server"></asp:TextBox>
    <br />
    <br />
    Latitude&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <asp:TextBox ID="txtLat" runat="server"></asp:TextBox>
    <br />
    <br />
    <br />
    Duration of Event     Starts
    <asp:TextBox ID="txtEventStarts" runat="server"></asp:TextBox>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <asp:Label ID="lblEnds" runat="server" Text="Ends"></asp:Label>&nbsp;&nbsp;<asp:TextBox ID="txtEnds" runat="server"></asp:TextBox>
    <br />
    <br />
    <br />
    Comments &nbsp;&nbsp;
    <asp:TextBox ID="txtComments" runat="server" Height="65px" Width="813px"></asp:TextBox>
    <br />
    <br />
    <br />
    <%--&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--%>
    <asp:Button ID="btnSubmit" runat="server" Text="Submit" OnClick="btnSubmit_Click" />
    <br />
</asp:Content>
