<%@ page language="java" contentType="text/html; charset=utf-8"
	pageEncoding="utf-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>

<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8" />
<meta name="viewport"
	content="width=device-width, initial-scale=1, shrink-to-fit=no">
<link rel="apple-touch-icon" sizes="76x76"
	href="<c:url value="/assets/img/apple-icon.png"/>">
<link rel="icon" type="image/png"
	href="<c:url value="/assets/img/favicon.png"/>">
<title>Power Security - Authentication</title>
<link rel="stylesheet" type="text/css"
	href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900|Roboto+Slab:400,700" />
<link href="<c:url value="/assets/css/nucleo-icons.css"/>"
	rel="stylesheet" />
<link href="<c:url value="/assets/css/nucleo-svg.css"/>"
	rel="stylesheet" />
<script src="https://kit.fontawesome.com/42d5adcbca.js"
	crossorigin="anonymous"></script>
<link
	href="https://fonts.googleapis.com/icon?family=Material+Icons+Round"
	rel="stylesheet">
<link id="pagestyle"
	href="<c:url value="/assets/css/material-dashboard.css?v=3.0.0"/>"
	rel="stylesheet" />
</head>

<body class="bg-gray-200">
	<main class="main-content  mt-0">
		<div class="page-header align-items-start min-vh-100"
			style="background-image: url('https://images.unsplash.com/photo-1497294815431-9365093b7331?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1950&q=80');">
			<span class="mask bg-gradient-dark opacity-6"></span>
			<div class="container my-auto">
				<div class="row">
					<div class="col-lg-4 col-md-8 col-12 mx-auto">
						<div class="card z-index-0 fadeIn3 fadeInBottom">
							<div
								class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
								<div
									class="bg-gradient-primary shadow-primary border-radius-lg py-3 pe-1">
									<h4 class="text-white font-weight-bolder text-center mt-2 mb-0">Power
										Security</h4>
								</div>
							</div>
							<div class="card-body">
								<form role="form" class="text-start" method="POST"
									action="/login">
									<div class="input-group input-group-outline my-3">
										<label class="form-label">Username</label> <input type="text"
											class="form-control" name="username" value="">
									</div>
									<div class="input-group input-group-outline mb-3">
										<label class="form-label">Password</label> <input
											type="password" class="form-control" name="password" value="">
									</div>
									<div
										class="form-check form-switch d-flex align-items-center mb-3">
										<input class="form-check-input" type="checkbox"
											id="rememberMe" name="rememberme"> <label
											class="form-check-label mb-0 ms-2" for="rememberMe">Remember
											me</label>
									</div>
									<div class="text-center">
										<button type="submit"
											class="btn bg-gradient-primary w-100 my-4 mb-2">Sign
											in</button>
									</div>
								</form>
								<c:if test="${error}">
									<div class="alert alert-danger">
										<div class="card">
											<div class="card-body">
												<p style="color:red;font-size:20px;">Username or password are invalid</p>
											</div>
										</div>
									</div>
								</c:if>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</main>
	<!--   Core JS Files   -->
	<script src="<c:url value="/assets/js/core/popper.min.js"/>"></script>
	<script src="<c:url value="/assets/js/core/bootstrap.min.js"/>"></script>
	<script
		src="<c:url value="/assets/js/plugins/perfect-scrollbar.min.js"/>"></script>
	<script
		src="<c:url value="/assets/js/plugins/smooth-scrollbar.min.js"/>"></script>
	<script>
		var win = navigator.platform.indexOf('Win') > -1;
		if (win && document.querySelector('#sidenav-scrollbar')) {
			var options = {
				damping : '0.5'
			}
			Scrollbar.init(document.querySelector('#sidenav-scrollbar'),
					options);
		}
	</script>

	<script
		src="<c:url value="/assets/js/material-dashboard.min.js?v=3.0.0"/>"></script>
</body>

</html>