# coding: utf-8

"""
    Skill Repository

    The API description of the Skill Repository.  # noqa: E501

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PathFinderApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def path_finder_controller_compute_path(self, body, **kwargs):  # noqa: E501
        """path_finder_controller_compute_path  # noqa: E501

        Computes the optimal learning path to learn the specified skill(s).  Parameters: - goal (mandatory): The list of skills to be learned. - userId (optional): If specified, path will be computed and optimized for the specified user, e.g., considering learned skills and learning behavior. - optimalSolution (optional): If unspecified, algorithm will use a fast, greedy approach to find a path. If true, the algorithm will try to find an optimal path, at cost of performance.     Default path for learning Java (skill 1009) ```json {   \"goal\": [\"1009\"] } ```  Path for learning DigiMedia (skills 2501 - 2512) for user 2001, ensure performant computation ```json {   \"goal\": [\"2501\", \"2502\", \"2503\", \"2504\", \"2505\", \"2506\", \"2507\", \"2508\", \"2509\", \"2510\", \"2511\", \"2512\"],   \"userId\": \"2001\",   \"optimalSolution\": false } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_compute_path(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PathRequestDto body: (required)
        :return: PathDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.path_finder_controller_compute_path_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.path_finder_controller_compute_path_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def path_finder_controller_compute_path_with_http_info(self, body, **kwargs):  # noqa: E501
        """path_finder_controller_compute_path  # noqa: E501

        Computes the optimal learning path to learn the specified skill(s).  Parameters: - goal (mandatory): The list of skills to be learned. - userId (optional): If specified, path will be computed and optimized for the specified user, e.g., considering learned skills and learning behavior. - optimalSolution (optional): If unspecified, algorithm will use a fast, greedy approach to find a path. If true, the algorithm will try to find an optimal path, at cost of performance.     Default path for learning Java (skill 1009) ```json {   \"goal\": [\"1009\"] } ```  Path for learning DigiMedia (skills 2501 - 2512) for user 2001, ensure performant computation ```json {   \"goal\": [\"2501\", \"2502\", \"2503\", \"2504\", \"2505\", \"2506\", \"2507\", \"2508\", \"2509\", \"2510\", \"2511\", \"2512\"],   \"userId\": \"2001\",   \"optimalSolution\": false } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_compute_path_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PathRequestDto body: (required)
        :return: PathDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method path_finder_controller_compute_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `path_finder_controller_compute_path`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/PathFinder/computePath', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PathDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def path_finder_controller_enrollment(self, body, **kwargs):  # noqa: E501
        """path_finder_controller_enrollment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_enrollment(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EnrollmentRequestDto body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.path_finder_controller_enrollment_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.path_finder_controller_enrollment_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def path_finder_controller_enrollment_with_http_info(self, body, **kwargs):  # noqa: E501
        """path_finder_controller_enrollment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_enrollment_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EnrollmentRequestDto body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method path_finder_controller_enrollment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `path_finder_controller_enrollment`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/PathFinder/adapted-path', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def path_finder_controller_enrollment_by_goal(self, body, **kwargs):  # noqa: E501
        """path_finder_controller_enrollment_by_goal  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_enrollment_by_goal(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomCourseRequestDto body: (required)
        :return: CustomCoursePreviewResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.path_finder_controller_enrollment_by_goal_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.path_finder_controller_enrollment_by_goal_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def path_finder_controller_enrollment_by_goal_with_http_info(self, body, **kwargs):  # noqa: E501
        """path_finder_controller_enrollment_by_goal  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_enrollment_by_goal_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomCourseRequestDto body: (required)
        :return: CustomCoursePreviewResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method path_finder_controller_enrollment_by_goal" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `path_finder_controller_enrollment_by_goal`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/PathFinder/calculated-path', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomCoursePreviewResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def path_finder_controller_simulate_enrollment(self, user_id, learning_path_id, optimal_solution, **kwargs):  # noqa: E501
        """path_finder_controller_simulate_enrollment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_simulate_enrollment(user_id, learning_path_id, optimal_solution, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param str learning_path_id: (required)
        :param bool optimal_solution: (required)
        :return: EnrollmentPreviewResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.path_finder_controller_simulate_enrollment_with_http_info(user_id, learning_path_id, optimal_solution, **kwargs)  # noqa: E501
        else:
            (data) = self.path_finder_controller_simulate_enrollment_with_http_info(user_id, learning_path_id, optimal_solution, **kwargs)  # noqa: E501
            return data

    def path_finder_controller_simulate_enrollment_with_http_info(self, user_id, learning_path_id, optimal_solution, **kwargs):  # noqa: E501
        """path_finder_controller_simulate_enrollment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_simulate_enrollment_with_http_info(user_id, learning_path_id, optimal_solution, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param str learning_path_id: (required)
        :param bool optimal_solution: (required)
        :return: EnrollmentPreviewResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'learning_path_id', 'optimal_solution']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method path_finder_controller_simulate_enrollment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `path_finder_controller_simulate_enrollment`")  # noqa: E501
        # verify the required parameter 'learning_path_id' is set
        if ('learning_path_id' not in params or
                params['learning_path_id'] is None):
            raise ValueError("Missing the required parameter `learning_path_id` when calling `path_finder_controller_simulate_enrollment`")  # noqa: E501
        # verify the required parameter 'optimal_solution' is set
        if ('optimal_solution' not in params or
                params['optimal_solution'] is None):
            raise ValueError("Missing the required parameter `optimal_solution` when calling `path_finder_controller_simulate_enrollment`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('userId', params['user_id']))  # noqa: E501
        if 'learning_path_id' in params:
            query_params.append(('learningPathId', params['learning_path_id']))  # noqa: E501
        if 'optimal_solution' in params:
            query_params.append(('optimalSolution', params['optimal_solution']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/PathFinder/adapted-path', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EnrollmentPreviewResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def path_finder_controller_simulate_enrollment_by_goal(self, user_id, goals, optimal_solution, **kwargs):  # noqa: E501
        """path_finder_controller_simulate_enrollment_by_goal  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_simulate_enrollment_by_goal(user_id, goals, optimal_solution, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param list[str] goals: (required)
        :param bool optimal_solution: (required)
        :return: EnrollmentPreviewResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.path_finder_controller_simulate_enrollment_by_goal_with_http_info(user_id, goals, optimal_solution, **kwargs)  # noqa: E501
        else:
            (data) = self.path_finder_controller_simulate_enrollment_by_goal_with_http_info(user_id, goals, optimal_solution, **kwargs)  # noqa: E501
            return data

    def path_finder_controller_simulate_enrollment_by_goal_with_http_info(self, user_id, goals, optimal_solution, **kwargs):  # noqa: E501
        """path_finder_controller_simulate_enrollment_by_goal  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_simulate_enrollment_by_goal_with_http_info(user_id, goals, optimal_solution, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param list[str] goals: (required)
        :param bool optimal_solution: (required)
        :return: EnrollmentPreviewResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'goals', 'optimal_solution']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method path_finder_controller_simulate_enrollment_by_goal" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `path_finder_controller_simulate_enrollment_by_goal`")  # noqa: E501
        # verify the required parameter 'goals' is set
        if ('goals' not in params or
                params['goals'] is None):
            raise ValueError("Missing the required parameter `goals` when calling `path_finder_controller_simulate_enrollment_by_goal`")  # noqa: E501
        # verify the required parameter 'optimal_solution' is set
        if ('optimal_solution' not in params or
                params['optimal_solution'] is None):
            raise ValueError("Missing the required parameter `optimal_solution` when calling `path_finder_controller_simulate_enrollment_by_goal`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('userId', params['user_id']))  # noqa: E501
        if 'goals' in params:
            query_params.append(('goals', params['goals']))  # noqa: E501
            collection_formats['goals'] = 'multi'  # noqa: E501
        if 'optimal_solution' in params:
            query_params.append(('optimalSolution', params['optimal_solution']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/PathFinder/calculated-path', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EnrollmentPreviewResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def path_finder_controller_skill_analysis(self, body, **kwargs):  # noqa: E501
        """path_finder_controller_skill_analysis  # noqa: E501

        Analysis a skill (goal) to find the missing skills in the learning path.  Parameters: - goal (mandatory): The list of skills to be learned.  Returns: - If the return path is empty, then there are no learning units for the skill.      Default path for learning Java (skill 1009) ```json { \"goal\": [\"1009\"] } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_skill_analysis(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SkillsToAnalyze body: (required)
        :return: SubPathListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.path_finder_controller_skill_analysis_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.path_finder_controller_skill_analysis_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def path_finder_controller_skill_analysis_with_http_info(self, body, **kwargs):  # noqa: E501
        """path_finder_controller_skill_analysis  # noqa: E501

        Analysis a skill (goal) to find the missing skills in the learning path.  Parameters: - goal (mandatory): The list of skills to be learned.  Returns: - If the return path is empty, then there are no learning units for the skill.      Default path for learning Java (skill 1009) ```json { \"goal\": [\"1009\"] } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_skill_analysis_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SkillsToAnalyze body: (required)
        :return: SubPathListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method path_finder_controller_skill_analysis" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `path_finder_controller_skill_analysis`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/PathFinder/skillAnalysis', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SubPathListDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def path_finder_controller_store_personalized_path(self, body, user_id, **kwargs):  # noqa: E501
        """Experimental (WIP)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_store_personalized_path(body, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PathStorageRequestDto body: (required)
        :param str user_id: (required)
        :return: PathStorageResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.path_finder_controller_store_personalized_path_with_http_info(body, user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.path_finder_controller_store_personalized_path_with_http_info(body, user_id, **kwargs)  # noqa: E501
            return data

    def path_finder_controller_store_personalized_path_with_http_info(self, body, user_id, **kwargs):  # noqa: E501
        """Experimental (WIP)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_store_personalized_path_with_http_info(body, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PathStorageRequestDto body: (required)
        :param str user_id: (required)
        :return: PathStorageResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method path_finder_controller_store_personalized_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `path_finder_controller_store_personalized_path`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `path_finder_controller_store_personalized_path`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/PathFinder/{userId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PathStorageResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
